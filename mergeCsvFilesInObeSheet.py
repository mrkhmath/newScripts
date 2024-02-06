import pandas as pd
import os
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Define the folder containing the CSV files
folder_path = 'C:/Users/kh_ma/Downloads/g9Marks'


# Create a new workbook and select the active worksheet
workbook = Workbook()
sheet = workbook.active

# Loop through all the files in the folder
for file in os.listdir(folder_path):
    # Check if the file is a CSV
    if file.endswith('.csv'):
        file_path = os.path.join(folder_path, file)
        
        # Read the first sheet of the CSV file
        df = pd.read_csv(file_path)
        
        # If it's the first file, write the headers
        if file == os.listdir(folder_path)[0]:
            for col_num, column_title in enumerate(df.columns, 1):
                sheet.cell(row=1, column=col_num, value=column_title)
        
        # Write the data
        for row in dataframe_to_rows(df, index=False, header=False):
            sheet.append(row)

# Save the workbook
new_workbook_path = 'C:\\Users\\kh_ma\\Downloads\\g9Marks\\new_workbook.xlsx'
workbook.save(filename=new_workbook_path)

print(f'Workbook created successfully at {new_workbook_path}')
