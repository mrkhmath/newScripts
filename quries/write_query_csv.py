# The complete Python code to read the CSV and generate the SQL insert queries is as follows:

import pandas as pd

# Function to read the CSV file and correct the pupilnumber format
def read_and_correct_csv(file_path):
    df = pd.read_csv(file_path)
    # Convert the pupilnumber column to string and remove any decimals
    df['pupilnumber'] = df['pupilnumber'].astype(str).str.split('.').str[0]
    return df

# Function to generate SQL insert queries from a pandas DataFrame
def generate_insert_queries(table_name, df):
    queries = []
    for index, row in df.iterrows():
        # Convert all values to strings, quote strings, and leave integers unquoted
        row_values = ["'{}'".format(value) if isinstance(value, str) else str(value) for value in row]
        query = "INSERT INTO {} ({}) VALUES ({});".format(table_name, ', '.join(df.columns), ', '.join(row_values))
        queries.append(query)
    return queries

# Read the CSV file
file_path = 'C:\\Users\\kh_ma\\Downloads\\df_summary.csv'
df_summary = read_and_correct_csv(file_path)

# Generate the SQL insert queries
table_name = 'credithours'
insert_queries = generate_insert_queries(table_name, df_summary)

# Save the queries to a .sql file
insert_queries_file_path = 'C:\\Users\\kh_ma\\Downloads\\insert_credithours_queries_complete.sql'
with open(insert_queries_file_path, 'w') as f:
    for query in insert_queries:
        f.write(query + '\n')

insert_queries_file_path
