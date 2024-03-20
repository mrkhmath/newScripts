import csv
import pandas as pd

# Mapping of subject names
subject_mapping = {
    "English Language": "English",
    "Arabic Language": "Arabic",
    "Mathematics ": "Math",
    "Moral Education": "Moral St",
    "Music": "Music",
    "Islamic Education": "Islamic",
    "Art": "Art",
    "Physical Education": "PE",
    "UAE Social Studies": "Social St",
    "Information and Communication Technology (ICT)": "Technology",
    "Science": "Science",
    "Drama": "Drama"
}

input_file_name = 'C:\\Users\\kh_ma\\Documents\\scripts\\DataAnalysis\\MarkEnteredReport 23T2.csv'
output_file_name = 'C:\\Users\\kh_ma\\Documents\\scripts\\DataAnalysis\\updated_MarkEnteredReport 23T2.csv'

# Open the input file and an output file
with open(input_file_name, mode='r', encoding='utf-8') as infile, open(output_file_name, mode='w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    if "Subject Name" not in fieldnames:
        raise ValueError("CSV does not contain a 'Subject Name' column.")

    # Assuming "Homeroom" is a column, include it in the check
    homeroom_exists = "Homeroom" in fieldnames
    
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        # Update subject name
        if row["Subject Name"] in subject_mapping:
            row["Subject Name"] = subject_mapping[row["Subject Name"]]
        
        # Update homeroom value if applicable
        if homeroom_exists and row["Homeroom"].startswith("G"):
            # Remove the first character "G"
            row["Homeroom"] = row["Homeroom"][1:]
            # Remove "th -" if present
            row["Homeroom"] = row["Homeroom"].replace("-", "")
        
        writer.writerow(row)


original_df = pd.read_csv('C:\\Users\\kh_ma\\Documents\\scripts\\DataAnalysis\\updated_MarkEnteredReport 23T2.csv')
teachers_df = pd.read_csv('C:\\Users\\kh_ma\\Documents\\scripts\\DataAnalysis\\teachers.csv')


# Adjust the column name in the following line to match the actual homeroom column name in your teachers.csv file
homeroom_column_name = 'Homeroom'  # Replace 'Homeroom' with the actual column name

# Define a function to find the teacher based on Homeroom and Subject Name
def find_teacher(homeroom, subject_name):
    # Filter the teachers DataFrame for the row with the matching Homeroom
    filtered_teachers = teachers_df[teachers_df[homeroom_column_name] == homeroom]
   
    # Iterate through the columns in the filtered teachers DataFrame to find the matching subject
    for column in filtered_teachers.columns:
        # Make sure to exclude the column used for matching homeroom values
       
        if column != homeroom_column_name and column == subject_name:
            # Return the teacher's name if a match is found
            
            return filtered_teachers[subject_name].iloc[0]
    # Return None if no match is found
    return None

# Add a new column 'Teacher' to the original DataFrame, using the find_teacher function to determine the values
original_df['Teacher'] = original_df.apply(lambda row: find_teacher(row['Homeroom'], row['Subject Name']), axis=1)

# Overwrite the original CSV file with the updated DataFrame
original_df.to_csv('C:\\Users\\kh_ma\\Documents\\scripts\\DataAnalysis\\updated_MarkEnteredReport 23T2.csv', index=False)

print("Subjects and Homeroom values updated successfully.")
