#!/usr/bin/env python3

import warnings
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import argparse
import numpy as np
from helpers import upload_df_to_gcs

warnings.simplefilter(action="ignore", category=FutureWarning)

pd.options.mode.chained_assignment = None


def get_args():
    """
    Gets arguments from command line
    Returns:
        args: arguments from command line
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument(
        "--match_id",
        help="Match Id of match to retrieve data",
        type=int,
        required=True,
    )

    return args_parser.parse_args()


def get_scorecard(series_id, match_id):
    URL = (
        "https://www.espncricinfo.com/series/"
        + str(series_id)
        + "/scorecard/"
        + str(match_id)
    )
    page = requests.get(URL)
    bs = BeautifulSoup(page.content, "lxml")

    table_body = bs.find_all("tbody")
    bowler_df = pd.DataFrame(
        columns=[
            "Name",
            "Overs",
            "Maidens",
            "Runs",
            "Wickets",
            "Econ",
            "Dots",
            "4s",
            "6s",
            "Wd",
            "Nb",
            "Team",
            "Player_id",
        ]
    )
    for i, table in enumerate(table_body[1:4:2]):
        if len(table.find_all(True, {"class": "font-weight-bold match-venue"})) == 0:
            rows = table.find_all("tr")
            for row in rows:
                player_id_col = row.find_all("a", href=True)
                if len(player_id_col) > 0 and "cricketers" in player_id_col[0]["href"]:
                    player_id = player_id_col[0]["href"].split("-")[-1]
                    cols = row.find_all("td")
                    cols = [x.text.strip() for x in cols]
                    bowler_df = bowler_df.append(
                        pd.Series(
                            [
                                re.sub(r"\W+", " ", cols[0]).strip(),
                                cols[1],
                                cols[2],
                                cols[3],
                                cols[4],
                                cols[5],
                                cols[6],
                                cols[7],
                                cols[8],
                                cols[9],
                                cols[10],
                                (i == 0) + 1,
                                player_id,
                            ],
                            index=bowler_df.columns,
                        ),
                        ignore_index=True,
                    )

    batsmen_df = pd.DataFrame(
        columns=["Name", "Desc", "Runs", "Balls", "4s", "6s", "SR", "Team", "Player_id"]
    )
    for i, table in enumerate(table_body[0:4:2]):
        rows = table.find_all("tr")
        for row in rows:
            player_id_col = row.find_all("a", href=True)
            if len(player_id_col) > 0:
                player_id = player_id_col[0]["href"].split("-")[-1]
            cols = row.find_all("td")
            cols = [x.text.strip() for x in cols]
            if cols[0] == "Extras" or cols[0] == "TOTAL":
                continue
            if len(cols) > 1 and cols[1] == "absent hurt":
                batsmen_df = batsmen_df.append(
                    pd.Series(
                        [
                            re.sub(r"\W+", " ", cols[0].split("(c)")[0]).strip(),
                            cols[1],
                            0,
                            0,
                            0,
                            0,
                            0,
                            i + 1,
                            player_id,
                        ],
                        index=batsmen_df.columns,
                    ),
                    ignore_index=True,
                )
            if len(cols[0].split("Did not bat")) > 1:
                cols = row.find_all("td")
                player_id_col = cols[0].find_all("a", href=True)
                player_ids = [player["href"].split("-")[-1] for player in player_id_col]
                dnb_cols = cols[0].find_all("span")
                dnb = [x.text.strip().split("(c)")[0] for x in dnb_cols]
                dnb = [re.sub(r"\W+", " ", x).strip() for x in dnb]
                dnb = [x for x in dnb if not bool(re.search(r"\d", x)) and x != ""]
                dnb = [i for n, i in enumerate(dnb) if i not in dnb[:n]]
                for idx, dnb_batsman in enumerate(dnb):
                    batsmen_df = batsmen_df.append(
                        pd.Series(
                            [dnb_batsman, "DNB", 0, 0, 0, 0, 0, i + 1, player_ids[idx]],
                            index=batsmen_df.columns,
                        ),
                        ignore_index=True,
                    )

            elif len(cols) > 2:
                batsmen_df = batsmen_df.append(
                    pd.Series(
                        [
                            re.sub(r"\W+", " ", cols[0].split("(c)")[0]).strip(),
                            cols[1],
                            cols[2],
                            cols[3],
                            cols[5],
                            cols[6],
                            cols[7],
                            i + 1,
                            player_id,
                        ],
                        index=batsmen_df.columns,
                    ),
                    ignore_index=True,
                )

    ## Point calculation
    bowler_df["Wickets"] = bowler_df["Wickets"].astype(int)
    bowler_df["Runs"] = bowler_df["Runs"].astype(int)
    bowler_df["Dots"] = bowler_df["Dots"].astype(int)
    bowler_df["Maidens"] = bowler_df["Maidens"].astype(int)
    bowler_df["Balls"] = (
        bowler_df["Overs"]
        .apply(lambda x: x.split("."))
        .apply(lambda x: int(x[0]) * 6 + int(x[1]) if len(x) > 1 else int(x[0]) * 6)
    )

    bowler_df["base_points"] = 20 * bowler_df["Wickets"]
    bowler_df["pace_points"] = 1.5 * bowler_df["Balls"] - bowler_df["Runs"]
    bowler_df["pace_points"] = (
        bowler_df["pace_points"]
        + (bowler_df.loc[:, "pace_points"] > 0) * bowler_df["pace_points"]
    ).astype(int)
    bowler_df["milestone_points"] = bowler_df["Wickets"].replace(
        {1: 0, 2: 5, 3: 15, 4: 30, 5: 50, 6: 50, 7: 50, 8: 50}
    )
    bowler_df["impact_points"] = bowler_df["Dots"] + bowler_df["Maidens"] * 25
    bowler_df["bowling_points"] = (
        bowler_df["base_points"]
        + bowler_df["pace_points"]
        + bowler_df["milestone_points"]
        + bowler_df["impact_points"]
    )

    batsmen_df["Runs"] = batsmen_df["Runs"].astype(int)
    batsmen_df["Balls"] = batsmen_df["Balls"].astype(int)
    batsmen_df["4s"] = batsmen_df["4s"].astype(int)
    batsmen_df["6s"] = batsmen_df["6s"].astype(int)
    batsmen_df["base_points"] = batsmen_df["Runs"]
    batsmen_df["pace_points"] = batsmen_df["Runs"] - batsmen_df["Balls"]
    batsmen_df["milestone_points"] = (np.floor(batsmen_df["Runs"] / 25)).replace(
        {1.0: 5, 2.0: 15, 3.0: 30, 4.0: 50, 5.0: 50, 6.0: 50, 7.0: 50, 8.0: 50}
    )
    batsmen_df["impact_points"] = (
        batsmen_df["4s"]
        + 2 * batsmen_df["6s"]
        + (batsmen_df["Runs"] == 0)
        * (batsmen_df["Desc"] != "not out")
        * (batsmen_df["Desc"] != "DNB")
        * (batsmen_df["Desc"] != "absent hurt")
        * (-5)
    )
    batsmen_df["batting_points"] = (
        batsmen_df["base_points"]
        + batsmen_df["pace_points"]
        + batsmen_df["milestone_points"]
        + batsmen_df["impact_points"]
    )

    teams_df = (
        pd.concat(
            [
                batsmen_df[["Name", "Team", "Player_id"]],
                bowler_df[["Name", "Team", "Player_id"]],
            ]
        )
        .drop_duplicates()
        .reset_index(drop=True)
    )

    fielder_df = teams_df.copy()
    fielder_df.loc[:, "fielding_points"] = 0
    for team in [1, 2]:
        fielders = []
        for wicket in batsmen_df[batsmen_df["Team"] == team]["Desc"]:
            if wicket.find("c & b") == 0:
                fielders.append(wicket.split("c & b")[1].strip())
            elif wicket.find("c") == 0:
                fielders.append(wicket.split("c ")[1].split(" b ")[0].strip())
            if wicket.find("st") == 0:
                fielders.append(wicket.split("st ")[1].split(" b ")[0].strip())
            if wicket.find("run out") == 0:
                fielders.extend(
                    [
                        x.strip()
                        for x in wicket.split("run out")[1]
                        .replace("(", "")
                        .replace(")", "")
                        .split("/")
                    ]
                )

        fielders = list(
            filter(lambda x: "sub (" not in x and "sub [" not in x, fielders)
        )
        fielders = [re.sub(r"\W+", " ", fielder).strip() for fielder in fielders]
        fielding_team = [1 if team == 2 else 2]
        for fielder in fielders:
            s = fielder_df.loc[fielder_df["Team"] == fielding_team[0]][
                "Name"
            ].str.contains(fielder)
            if len(s[s].index.values) > 0:  ## Entire name matches
                index_val = s[s].index.values[0]
            elif (
                fielder_df["Name"].str.contains(fielder.split()[1]).sum() == 1
            ):  ## Second name matches with exactly one player
                s = fielder_df["Name"].str.contains(fielder.split()[1])
                index_val = s[s].index.values[0]
            elif (
                (fielder_df["Name"].str.contains(fielder.split()[1]))
                & (fielder_df["Name"].str[0] == fielder.split()[0][0])
            ).sum() == 1:  ## Check for second name match and match of first letter of initial with first letter of name
                s = (fielder_df["Name"].str.contains(fielder.split()[1])) & (
                    fielder_df["Name"].str[0] == fielder.split()[0][0]
                )
                index_val = s[s].index.values[0]
            elif (
                fielder_df["Name"].str.contains(fielder.split()[0]).sum() == 1
            ):  ## First name matches with exactly one player
                s = fielder_df["Name"].str.contains(fielder.split()[0])
                index_val = s[s].index.values[0]
            else:
                print("MoM not found")
            fielder_df.loc[index_val, "fielding_points"] += 10

    ### MOM
    fielder_df.loc[:, "bonus_points"] = 0
    for item in bs.find_all(
        "div", {"class": "ds-flex ds-justify-between ds-items-center"}
    ):
        if "Player Of The Match" in item.text:
            mom_id = item.find("a")["href"].split("-")[-1]
    fielder_df.loc[fielder_df["Player_id"] == mom_id, "bonus_points"] += 25

    ### Winning team points
    if table_body[4].find_all("tr")[-1].find_all("td")[0].text == "Points":
        match_points = table_body[4].find_all("tr")[-1].find_all("td")[1].text
        team_name_index = {
            bs.find_all(
                "span", {"class": "ds-text-title-xs ds-font-bold ds-capitalize"}
            )[0].text: 1,
            bs.find_all(
                "span", {"class": "ds-text-title-xs ds-font-bold ds-capitalize"}
            )[1].text: 2,
        }
        if match_points.find("2") != -1:
            winner = match_points.split("2")[0].strip()
            winner_index = team_name_index[winner]
            fielder_df.loc[fielder_df["Team"] == winner_index, "bonus_points"] += 5

    total_df = (
        teams_df.merge(batsmen_df, how="left", on=["Name", "Player_id", "Team"])
        .merge(
            bowler_df, how="left", on=["Player_id"], suffixes=("_batting", "_bowling")
        )
        .merge(fielder_df, how="left", on=["Player_id"])
        .fillna(0)
    )

    total_df["total_points"] = (
        total_df["batting_points"]
        + total_df["bowling_points"]
        + total_df["fielding_points"]
        + total_df["bonus_points"]
    )

    total_df = total_df.reset_index()

    # Save df
    total_df.to_csv(f"./Scorecards/{match_id}_scorecard.csv", header=True, index=False)

    return total_df


if __name__ == "__main__":

    args = get_args()
    df = get_scorecard(8048, args.match_id)
    upload_df_to_gcs(df, f"Scorecards/{args.match_id}_scorecard.csv")
