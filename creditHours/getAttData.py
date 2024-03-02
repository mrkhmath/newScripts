import psycopg2
from psycopg2 import sql
import pandas as pd
from datetime import datetime, timedelta

# Connect to your PostgreSQL database
conn =psycopg2.connect(
    dbname="vmxtdgqf", 
    user="vmxtdgqf", 
    password="WP_sencWINUN3Ry7Gy-u4qH9iC6rcnLI", 
    host="rogue.db.elephantsql.com", 
    port="5432"
)

# Function to check if a table exists
def check_table_exists(conn, table_name):
    cur = conn.cursor()
    cur.execute(sql.SQL("SELECT EXISTS (SELECT FROM pg_tables WHERE tablename = %s);"), [table_name])
    exists = cur.fetchone()[0]
    cur.close()
    return exists

# Lists to hold DataFrames for attendance and subjects
dfs_att = []
dfs_sub = []
dfs_sub_filtered=[]
# Generate date range
start_date = datetime(2023, 11, 27)
# start_date = datetime(2024, 1, 29)
end_date = datetime(2024, 2, 29)

current_date = start_date
while current_date <= end_date:
    # Skip weekends
    if current_date.weekday() < 5:  # 0 is Monday, 6 is Sunday
        table_name = 'zatt' + current_date.strftime('%Y%m%d')
        if check_table_exists(conn, table_name):
            # Fetch attendance data
            query_att = sql.SQL("SELECT pupilnumber, p1, p2, p3, p4, p5, p6 FROM {}").format(sql.Identifier(table_name))
            df_att = pd.read_sql_query(query_att, conn)
            
            # Fetch subject data
            query_sub = sql.SQL("SELECT pupilnumber, p1sub, p2sub, p3sub, p4sub, p5sub, p6sub FROM {}").format(sql.Identifier(table_name))
            df_sub = pd.read_sql_query(query_sub, conn)
            
            # Create df_sub_filtered as a copy of df_sub
            df_sub_filtered = df_sub.copy()

            # Iterate over each period column to empty values based on attendance
            for period in range(1, 7):
                # Find indices where attendance is 0 or null
                mask = (df_att[f'p{period}'] == '0') | (df_att[f'p{period}']=='null')
                # Empty the corresponding subject values
                df_sub_filtered.loc[mask, f'p{period}sub'] = None  # or np.nan if you prefer
                
            # Add the date column
            df_sub_filtered['date'] = current_date
            
            # Append the filtered DataFrame to the list
            dfs_sub.append(df_sub)
            dfs_att.append(df_att)
            dfs_sub_filtered.append(df_sub_filtered)

    current_date += timedelta(days=1)
    
# Close the database connection

# Step 1: Extract unique pupil numbers
unique_pupil_numbers = pd.concat([df['pupilnumber'] for df in dfs_att]).unique()

# Step 2: Identify all unique subjects
unique_subjects = pd.concat([df[[f'p{period}sub' for period in range(1, 7)]] for df in dfs_sub_filtered]).melt()['value'].unique()
unique_subjects = [subject for subject in unique_subjects if pd.notnull(subject)]  # Remove NaN values

# Step 3: Create a new DataFrame
df_summary = pd.DataFrame({'pupilnumber': unique_pupil_numbers})
for subject in unique_subjects:
    df_summary[subject] = 0  # Initialize subject columns with 0

# Step 4: Populate the DataFrame by counting occurrences
for df in dfs_sub_filtered:
    for period in range(1, 7):
        period_sub = f'p{period}sub'
        # For each row, increment the subject count for the corresponding pupil number
        for index, row in df.iterrows():
            pupilnumber = row['pupilnumber']
            subject = row[period_sub]
            if pd.notnull(subject):  # Only count if subject is not null
                df_summary.loc[df_summary['pupilnumber'] == pupilnumber, subject] += 1

# df_summary now contains the count of each subject for each pupil number

df_summary.to_csv('C:\\Users\\kh_ma\\Downloads\\df_summary.csv', index=False)
# print(dfs_att[0])

conn.close()

# At this point, dfs contains all your DataFrames and they are also named dynamically like df_zatt20231127, df_zatt20231128, etc.
