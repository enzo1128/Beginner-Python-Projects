# great resource for dataframes in pandas: https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/#:~:text=Indexing%20in%20pandas%20means%20simply,be%20known%20as%20Subset%20Selection.
import csv
import pandas as pd
import gdown
import os
import subprocess
import requests
import json


pd.set_option('display.max_columns', None)
FILE_PATH = "/Users/Enzo/Desktop/Coding/untitled folder/Expense Claims Form (2022-2023 Responses) - Form responses 1.csv"
# when finished, replace with input()
COLUMNS_TO_EXTRACT = [1, 3, 4, 6, 9]

file = pd.read_csv(FILE_PATH)
subfile = file.iloc[:, COLUMNS_TO_EXTRACT]

new_col_names = ["name", "date", "type", "receipts", "location"]
subfile.columns = new_col_names
# /Users/Enzo/Desktop/Site\ Receitps

test_file = "/Users/Enzo/Desktop/Site Receitps/testfile.pdf"
link = subfile.iloc[2,3]
link = link.replace("open?id=", "uc?id=")
print(link)
gdown.download(link, test_file, quiet=False)
# subprocess.run(['open', test_file], check=True)

def scan_receipt(image):
    url = "https://ocr.asprise.com/api/v1/receipt"
    test_file = image
    res = requests.post(url,
                        data = {
                            'api_key': 'TEST',
                            'recognizer': 'auto',
                            'ref_no': 'ocr_python_123'
                        },
                        files = {
                            'file': open(test_file, "rb")
                        })
    with open("response2.json", "w") as f:
        json.dump(json.loads(res.text), f)

scan_receipt(test_file)
ready = input("Are you ready to delete?")
if ready == "y":
    os.remove(test_file)
else:
    pass
# for i in subfile.iloc[:, 3]:
#     if "," in i:
#         print(i)


