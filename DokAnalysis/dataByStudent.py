import pandas as pd

# Load the Excel file
file_path = 'C:/Users/kh_ma/Downloads/assessmentsDok.csv'
df = pd.read_csv(file_path)

# Function to aggregate grades based on subject, dok, and academic year
def sum_grades(df, subject, dok_values, academic_year):
    # Check if dok_values is a list to accommodate "3,4" needing to check both "3" and "4"
    if not isinstance(dok_values, list):
        dok_values = [dok_values]
    # Filter DataFrame based on conditions and sum grades
    filtered_df = df[(df['subject'] == subject) & 
                     (df['dok'].isin(dok_values)) & 
                     (df['academic_year'] == academic_year)&
                     (df['assessment_type'] == 'End of Term 1')]
    return filtered_df.groupby('esis')['grade'].sum().reset_index(name=f'Grade Total {academic_year} DOK{"_".join(map(str, dok_values))}')

# Unique ESIS DataFrame
unique_esis = df[['esis']].drop_duplicates()

def perSubject(sub):
        # Compute required aggregates
    grades_22_23_dok1 = sum_grades(df, sub, '1', '22-23')
    grades_23_24_dok1 = sum_grades(df, sub, '1', '23-24')
    grades_22_23_dok2 = sum_grades(df, sub, '2', '22-23')
    grades_23_24_dok2 = sum_grades(df, sub, '2', '23-24')
    grades_22_23_dok34 = sum_grades(df, sub, '3,4', '22-23')
    grades_23_24_dok34 = sum_grades(df, sub, '3,4', '23-24')

    # Merge the aggregates back with the unique ESIS DataFrame
    final_df = unique_esis
    for grades_df in [grades_22_23_dok1, grades_23_24_dok1, grades_22_23_dok2, grades_23_24_dok2, grades_22_23_dok34, grades_23_24_dok34]:
        final_df = pd.merge(final_df, grades_df, on='esis', how='left')

    # Assuming the rest of the DataFrame is already prepared as per previous steps
    # Delete rows with all blank values
    final_df.dropna(how='all', inplace=True)
    # Save the final DataFrame to a new Excel sheet
    output_file_path = 'C:/Users/kh_ma/Downloads/Agg'+sub+'.xlsx'
    with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
        final_df.to_excel(writer, sheet_name='Aggregated Grades', index=False)

    output_file_path

for s in ['math','science','english','arabic']:
    perSubject(s)