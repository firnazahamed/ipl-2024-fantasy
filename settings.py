weeks = {
    "Week1": {"matches": [str(1422119 + i) for i in range(10)]},
    "Week2": {"matches": [str(1422119 + i) for i in range(10, 18)]},
    "Week3": {"matches": [str(1422119 + i) for i in range(18, 29)]},
    "Week4": {"matches": [str(1422119 + i) for i in range(29, 38)]},
    "Week5": {"matches": [str(1422119 + i) for i in range(38, 48)]},
    "Week6": {"matches": [str(1422119 + i) for i in range(48, 57)]},
    "Week7": {"matches": [str(1422119 + i) for i in range(57, 70)]},
    # "Week8": {"matches": [str(1422119 + i) for i in range(4)]},
}

owner_team_dict = {
    "Mabbu": "Malayoor Mambattiyaans",
    "Siddhu": "Virumandies",
    "Bhar": "Galactic Federation",
    "Srini": "Jeipomda XI",
    "Saju": "The Wolfpack",
    "Abhi": "Kovai Rousers",
    "Jilla": "J Kullis",
    "Ash": "Come on Ash!",
    "Firi": "Fiery Dragons",
    "Shar": "Underdogs",
    "Vaithy": "Thayir Saadham",
}

player_id_dict = {
    "MS Dhoni": "28081",
    "Aravelly Avanish": "1408675",
    "Devon Conway": "379140",
    "Ruturaj Gaikwad": "1060380",
    "Ajinkya Rahane": "277916",
    "Shaik Rasheed": "1292497",
    "Sameer Rizvi": "1175489",
    "Moeen Ali": "8917",
    "Shivam Dube": "714451",
    "Rajvardhan Hangargekar": "1175429",
    "Ravindra Jadeja": "234675",
    "Ajay Mandal": "1059570",
    "Daryl Mitchell": "381743",
    "Rachin Ravindra": "959767",
    "Mitchell Santner": "502714",
    "Nishant Sindhu": "1292506",
    "Deepak Chahar": "447261",
    "Tushar Deshpande": "822553",
    "Mukesh Choudhary": "1125688",
    "Mustafizur Rahman": "330902",
    "Matheesha Pathirana": "1194795",
    "Simarjeet Singh": "1159722",
    "Prashant Solanki": "1252337",
    "Shardul Thakur": "475281",
    "Maheesh Theekshana": "1138316",
    "Rishabh Pant": "931581",
    "Abishek Porel": "1277545",
    "Ricky Bhui": "642531",
    "Swastik Chikara": "1403198",
    "Yash Dhull": "1292498",
    "Jake Fraser-McGurk": "1168049",
    "Shai Hope": "581379",
    "Kumar Kushagra": "1207295",
    "Prithvi Shaw": "1070168",
    "Tristan Stubbs": "595978",
    "David Warner": "219889",
    "Harry Brook": "911707",
    "Lalit Yadav": "930189",
    "Mitchell Marsh": "272450",
    "Axar Patel": "554691",
    "Sumit Kumar": "1159734",
    "Khaleel Ahmed": "942645",
    "Praveen Dubey": "777515",
    "Kuldeep Yadav": "559235",
    "Mukesh Kumar": "926851",
    "Anrich Nortje": "481979",
    "Vicky Ostwal": "1292520",
    "Rasikh Salam": "1161489",
    "Jhye Richardson": "774223",
    "Ishant Sharma": "236779",
    "Lungi Ngidi": "542023",
    "Shubman Gill": "1070173",
    "David Miller": "321777",
    "Robin Minz": "1350762",
    "Wriddhiman Saha": "279810",
    "Sai Sudharsan": "1151288",
    "M Shahrukh Khan": "719719",
    "Matthew Wade": "230193",
    "Kane Williamson": "277906",
    "Azmatullah Omarzai": "819429",
    "Abhinav Manohar": "778963",
    "Rashid Khan": "793463",
    "Vijay Shankar": "477021",
    "Manav Suthar": "1175426",
    "Rahul Tewatia": "423838",
    "Spencer Johnson": "1123718",
    "Kartik Tyagi": "1122918",
    "Josh Little": "928067",
    "Darshan Nalkande": "1111917",
    "Noor Ahmad": "1182529",
    "Sai Kishore": "1048739",
    "Mohit Sharma": "537119",
    "Umesh Yadav": "376116",
    "Jayant Yadav": "447587",
    "Mohammed Shami": "481896",
    "Sushant Mishra": "1175457",
    "Shreyas Iyer": "642519",
    "Srikar Bharat": "529436",
    "Manish Pandey": "290630",
    "Rahmanullah Gurbaz": "974087",
    "Ramandeep Singh": "1079470",
    "Nitish Rana": "604527",
    "Sherfane Rutherford": "914541",
    "Phil Salt": "669365",
    "Rinku Singh": "723105",
    "Jason Roy": "298438",
    "Venkatesh Iyer": "851403",
    "Sunil Narine": "230558",
    "Anukul Roy": "1079839",
    "Andre Russell": "276298",
    "Vaibhav Arora": "1209292",
    "Dushmantha Chameera": "552152",
    "Harshit Rana": "1312645",
    "Mujeeb Ur Rahman": "974109",
    "Chetan Sakariya": "1131754",
    "Mitchell Starc": "311592",
    "Suyash Sharma": "1350792",
    "Varun Chakravarthy": "1108375",
    "Gus Atkinson": "1039481",
    "Angkrish Raghuvanshi": "1292495",
    "Sakib Hussain": "1340422",
    "KL Rahul": "422108",
    "Ayush Badoni": "1151270",
    "Quinton de Kock": "379143",
    "Devdutt Padikkal": "1119026",
    "Nicholas Pooran": "604302",
    "Ashton Turner": "500268",
    "Krishnappa Gowtham": "424377",
    "Deepak Hooda": "497121",
    "Arshin Kulkarni": "1403153",
    "Prerak Mankad": "956871",
    "Kyle Mayers": "348056",
    "Krunal Pandya": "471342",
    "Marcus Stoinis": "325012",
    "David Willey": "308251",
    "Arshad Khan": "1244751",
    "Shamar Joseph": "1356971",
    "Amit Mishra": "31107",
    "Mohsin Khan": "1132005",
    "Naveen-ul-Haq": "793447",
    "Ravi Bishnoi": "1175441",
    "Shivam Mavi": "1079848",
    "Manimaran Siddharth": "1151286",
    "Mayank Yadav": "1292563",
    "Yash Thakur": "1070196",
    "Yudhvir Singh": "1206052",
    "Mark Wood": "351588",
    "Tim David": "892749",
    "Ishan Kishan": "720471",
    "Rohit Sharma": "34102",
    "Vishnu Vinod": "732293",
    "Nehal Wadhera": "1151273",
    "Suryakumar Yadav": "446507",
    "Hardik Pandya": "625371",
    "Dewald Brevis": "1070665",
    "Piyush Chawla": "32966",
    "Shreyas Gopal": "344580",
    "Anshul Kamboj": "1175428",
    "Mohammad Nabi": "25913",
    "Shams Mulani": "1131607",
    "Romario Shepherd": "677077",
    "Tilak Varma": "1170265",
    "Jasprit Bumrah": "625383",
    "Gerald Coetzee": "596010",
    "Kumar Kartikeya": "1159843",
    "Akash Madhwal": "1206039",
    "Dilshan Madushanka": "793007",
    "Arjun Tendulkar": "1148776",
    "Nuwan Thushara": "955235",
    "Luke Wood": "573170",
    "Jason Behrendorff": "272477",
    "Naman Dhir": "1287032",
    "Shivalik Sharma": "1167965",
    "Shikhar Dhawan": "28235",
    "Jonny Bairstow": "297433",
    "Harpreet Singh": "340854",
    "Prabhsimran Singh": "1161024",
    "Rilee Rossouw": "318845",
    "Jitesh Sharma": "721867",
    "Sam Curran": "662973",
    "Rishi Dhawan": "290727",
    "Liam Livingstone": "403902",
    "Shashank Singh": "377534",
    "Shivam Singh": "1380113",
    "Sikandar Raza": "299572",
    "Atharva Taide": "1125958",
    "Chris Woakes": "247235",
    "Arshdeep Singh": "1125976",
    "Rahul Chahar": "1064812",
    "Nathan Ellis": "826915",
    "Harpreet Brar": "1168641",
    "Vidwath Kaverappa": "1155262",
    "Harshal Patel": "390481",
    "Kagiso Rabada": "550215",
    "Prince Choudhary": "1412827",
    "Ashutosh Sharma": "1131978",
    "Vishwanath Singh": "1354639",
    "Tanay Thyagarajan": "1080008",
    "Sanju Samson": "425943",
    "Jos Buttler": "308967",
    "Shubham Dubey": "1252585",
    "Shimron Hetmyer": "670025",
    "Yashasvi Jaiswal": "1151278",
    "Dhruv Jurel": "1175488",
    "Tom Kohler-Cadmore": "470633",
    "Riyan Parag": "1079434",
    "Rovman Powell": "820351",
    "Kunal Singh Rathore": "1339031",
    "Abid Mushtaq": "1201536",
    "Ravichandran Ashwin": "26421",
    "Donovan Ferreira": "698315",
    "Avesh Khan": "694211",
    "Trent Boult": "277912",
    "Nandre Burger": "971349",
    "Yuzvendra Chahal": "430246",
    "Navdeep Saini": "700167",
    "Sandeep Sharma": "438362",
    "Kuldeep Sen": "1163695",
    "Adam Zampa": "379504",
    "Prasidh Krishna": "917159",
    "Faf du Plessis": "44828",
    "Anuj Rawat": "1123073",
    "Saurav Chauhan": "1287369",
    "Dinesh Karthik": "30045",
    "Virat Kohli": "253802",
    "Rajat Patidar": "823703",
    "Akash Deep": "1176959",
    "Manoj Bhandage": "1057399",
    "Tom Curran": "550235",
    "Cameron Green": "1076713",
    "Will Jacks": "897549",
    "Mahipal Lomror": "853265",
    "Glenn Maxwell": "325026",
    "Suyash Prabhudessai": "1083851",
    "Mayank Dagar": "942367",
    "Lockie Ferguson": "493773",
    "Alzarri Joseph": "670031",
    "Mohammed Siraj": "940973",
    "Rajan Kumar": "1339027",
    "Himanshu Sharma": "1350761",
    "Karn Sharma": "30288",
    "Swapnil Singh": "232292",
    "Reece Topley": "461632",
    "Vijaykumar Vyshak": "777815",
    "Yash Dayal": "1159720",
    "Abdul Samad": "1175485",
    "Mayank Agarwal": "398438",
    "Anmolpreet Singh": "851261",
    "Travis Head": "530011",
    "Heinrich Klaasen": "436757",
    "Aiden Markram": "600498",
    "Rahul Tripathi": "446763",
    "Upendra Yadav": "732269",
    "Abhishek Sharma": "1070183",
    "Wanindu Hasaranga": "784379",
    "Marco Jansen": "696401",
    "Nitish Kumar Reddy": "1175496",
    "Glenn Phillips": "823509",
    "Sanvir Singh": "1132219",
    "Shahbaz Ahmed": "1159711",
    "Washington Sundar": "719715",
    "Pat Cummins": "489889",
    "Akash Singh": "1175458",
    "Fazalhaq Farooqi": "974175",
    "Bhuvneshwar Kumar": "326016",
    "Mayank Markande": "1081442",
    "T Natarajan": "802575",
    "Jhathavedh Subramanyan": "919531",
    "Umran Malik": "1246528",
    "Jaydev Unadkat": "390484",
    "Kwena Maphaka": "1294342",
}

service_account_credentials = "credentials/cricinfo-273202-a7420ddc1abd.json"
squads_spreadsheet_url = "https://docs.google.com/spreadsheets/d/1KWLM_0V4QMZZrM62wRLAdY_5TkCg37nt3cFR8Mx67zU/"
unsold_spreadsheet_url = "https://docs.google.com/spreadsheets/d/1TaBtVrQYrHdaYGrAGlA61fhs6e7bYVctaQ_CD8v1nKo/"
trades_spreadsheet_url = "https://docs.google.com/spreadsheets/d/1ETA4v6Lb6cIWaR1WPaBhwEIet2Og7yipSL4WLrNh7TU/"
