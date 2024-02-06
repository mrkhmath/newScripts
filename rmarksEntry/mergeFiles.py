import pandas as pd
from tkinter import Tk, filedialog
import os

def select_excel_files():
    """Open a dialog to select Excel files and return the list of selected file paths."""
    root = Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(title="Select Excel files", filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    return root.tk.splitlist(file_paths)

def merge_first_sheet(excel_files):
    """Merge the first sheet of each selected Excel file into a new Excel file."""
    all_data = pd.DataFrame()

    for file_path in excel_files:
        # Read the first sheet automatically without specifying its name
        df = pd.read_excel(file_path, sheet_name=0)
        
        # Append the data from this sheet to the all_data DataFrame
        all_data = pd.concat([all_data, df], ignore_index=True)

    # Save the merged data to a new Excel file
    output_file = 'merged_sheets.xlsx'
    all_data.to_excel(output_file, index=False)
    print(f"Merged data saved to {output_file}")

def main():
    excel_files = select_excel_files()
    if excel_files:
        merge_first_sheet(excel_files)
    else:
        print("No files selected.")

if __name__ == "__main__":
    main()
