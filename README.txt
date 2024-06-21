Description:
The first script of this project loads a data source CSV file whose rows vincule multiple Myers–Briggs types to their respective internet posts (data tabe with 9000 row and 2 columns), and applies the MapReduce technique to determine the frequency on how each type appears in the 'type' row.
The outcome is another CSV file with only 16 rows followed by the number of time each type have been referenced in the 'type' row.
The second script of this project used Pandas Dataframes to extract statistical information from the mapreduce outcome.

The data source file was downloaded from 'Kaggle' web page.

How to run:
Call script using 'python main.py < "mbti.csv" > output.csv' in the command line from the project folder

Programing Language:
Python

IDE:
Pycharm Community Edition 2024.1.2

Operating System
Windows 10