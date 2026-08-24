#  this is a data cleaning application
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

data_path = ''
data_name = ''

# checking if the path exists
if not os.path.exists(data_path):
    print("Please Enter Correct Path. Try Again")
    # return

else:
    #  checking the file type 
    if data_path.endswith('.csv'):
        print('Dataset is CSV!')
        data = pd.read_csv(data_path, encoding_errors='ignore')

    elif data_path.endswith('xlsx'):
        print('Dataset is Excel file')
        data = pd.read_xlsx(data_path, encoding_errors='ignore')
    else:
        print("Unknown file type")

