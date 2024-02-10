import pandas as pd
from tkinter import Tk, filedialog

def select_csv_files():
    """Open a dialog to select CSV files and return the list of selected file paths."""
    root = Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(title="Select CSV files", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    return root.tk.splitlist(file_paths)

def merge_csv_files(csv_files):
    """Merge selected CSV files into a new Excel file."""
    all_data = pd.DataFrame()

    for file_path in csv_files:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Append the data from this CSV to the all_data DataFrame
        all_data = pd.concat([all_data, df], ignore_index=True)

    # Save the merged data to a new Excel file
    output_file = 'merged_data.xlsx'
    all_data.to_excel(output_file, index=False)
    print(f"Merged data saved to {output_file}")

def main():
    csv_files = select_csv_files()
    if csv_files:
        merge_csv_files(csv_files)
    else:
        print("No files selected.")

if __name__ == "__main__":
    main()
