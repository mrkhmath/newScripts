import pandas as pd

# Load the Excel file
all_data_df = pd.read_excel('C:/Users/kh_ma/Downloads/marksDescr.xlsx', sheet_name='allData')
esis_df = pd.read_excel('C:/Users/kh_ma/Downloads/marksDescr.xlsx', sheet_name='esis')

# Filter allData sheet where values in column B are included in column A of esis sheet
filtered_df = all_data_df[all_data_df['PUPIL NUMBER'].isin(esis_df['Column A'])]

# Save the filtered data to a new Excel file
filtered_df.to_excel('C:/Users/kh_ma/Downloads/filtered_allData.xlsx', index=False)
