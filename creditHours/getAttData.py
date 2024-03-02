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

# List to hold DataFrames
dfs = []

# Generate date range
start_date = datetime(2023, 11, 27)
# end_date = datetime(2024, 2, 29)
end_date = datetime(2023, 11, 27)

current_date = start_date
while current_date <= end_date:
    # Skip weekends
    if current_date.weekday() < 5:  # 0 is Monday, 6 is Sunday
        table_name = 'zatt' + current_date.strftime('%Y%m%d')
        if check_table_exists(conn, table_name):
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
            df = pd.read_sql_query(query, conn)
            # Dynamically name the DataFrame based on table_name
            globals()[f'df_{table_name}'] = df
            # Add the DataFrame to the list
            dfs.append(df)
    current_date += timedelta(days=1)

# Close the database connection
dfs[0].to_csv('C:\\Users\\kh_ma\\Downloads\\filename.csv', index=False)

conn.close()

# At this point, dfs contains all your DataFrames and they are also named dynamically like df_zatt20231127, df_zatt20231128, etc.
