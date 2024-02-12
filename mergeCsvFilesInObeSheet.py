import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import os

# Initialize tkinter
root = Tk()
# Hide the main window (optional)
root.withdraw()

# Open a file selection dialog to allow users to select CSV files
file_paths = askopenfilenames(filetypes=[("CSV files", "*.csv")])

# Initialize an empty DataFrame to hold data from all selected CSV files
combined_df = pd.DataFrame()

# Loop through the list of selected files
for file_path in file_paths:
    # Read each CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Append the data from this CSV into the combined DataFrame
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Write the combined DataFrame to a new Excel workbook
combined_df.to_excel('C:/Users/kh_ma/Downloads/combined_workbookAbdo.xlsx', index=False, engine='openpyxl')

# Print a success message
print(f"Files were successfully merged into combined_workbook.xlsx")
