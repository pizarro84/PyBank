# python-challenge
**PYTHON CHALLENGE** - This challenge contains two Python codes built to analyse financial data and poll results.

## Under Folder PyBank:
*"main.py" is the Python code and will process "budget_data.csv" file under Resources directory. The output file name is "ANALYSIS_PyBank_<csvName>_<DATETIMESTAMP>.txt".

*The file format should have a CSV header with the first column as the date (no date format necessary) and second column is the profit/loss value (profit is positive and loss is negative), data needs to be sorted by date from earliest to latest.

*The code will display the total number of monthly records in the CSV file, total of the monthly amount and the average change. The formula for the average change is sum of changes <current record - previous record> over number of changes (number of rows - 1).The code also displays the greatest increase and decrease in profits. The data is displayed on screen as well as written to an output file.

*To operate the code, place a csv file named "budget_data.csv" inside "Resources" directory. Run "python main.py" to generate an output file in the "analysis" directory.

## Under Folder PyPoll:
*"main.py" is the Python code and will process "election_data.csv" file under Resources directory. The output file name is "ANALYSIS_PyPoll_<csvName>_<DATETIMESTAMP>.txt".

*The file format should have a CSV header with "voter ID" in the first column, "county" in the second column and "candidate" in the third column.

*The code will count and display the number of votes for each specific candidate as well as the total number of votes. The percentage is calculated by dividing the candidate votes with total number of votes and multiplying by 100. The percentage value is rounded to the nearest one. The winner is determined by identifying the candidate with the greatest number of votes. The data is displayed on screen as well as written to an output file.

*To operate the code, place a csv file named "election_data.csv" inside "Resources" directory. Run "python main.py" to generate an output file in the "analysis" directory.
