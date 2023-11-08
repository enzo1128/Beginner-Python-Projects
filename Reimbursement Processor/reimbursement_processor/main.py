import csv
import pandas as pd
pd.set_option('display.max_columns', None)
FILE_PATH = "/Users/Enzo/Desktop/Coding/untitled folder/Expense Claims Form (2022-2023 Responses) - Form responses 1.csv"
# when finished, replace with input()
COLUMNS_TO_EXTRACT = [1, 3, 4, 6, 9]

file = pd.read_csv(FILE_PATH)
subfile = file.iloc[:, COLUMNS_TO_EXTRACT]

new_col_names = ["name", "date", "type", "receipts", "location"]
subfile.columns = new_col_names



print(subfile)


