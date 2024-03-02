from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta

# Database connection URL
db_url = 'postgresql+psycopg2://vmxtdgqf:WP_sencWINUN3Ry7Gy-u4qH9iC6rcnLI@rogue.db.elephantsql.com:5432/vmxtdgqf'

# Create an SQLAlchemy engine
engine = create_engine(db_url)

# List to hold DataFrames
dfs = []

# Generate date range
start_date = datetime(2023, 11, 27)
# end_date = datetime(2024, 2, 29)
end_date = datetime(2023, 11, 28)


current_date = start_date
while current_date <= end_date:
    # Skip weekends
    if current_date.weekday() < 5:  # 0 is Monday, 6 is Sunday
        table_name = f'zatt{current_date.strftime("%Y%m%d")}'
        query = f"SELECT * FROM {table_name}"
        # Check if the table exists by attempting to fetch from it
        try:
            df = pd.read_sql_query(query, engine)
            # Dynamically name the DataFrame based on table_name
            globals()[f'df_{table_name}'] = df
            # Add the DataFrame to the list
            dfs.append(df)
        except Exception as e:
            print(f"Could not load table {table_name}: {e}")
    current_date += timedelta(days=1)
print(dfs[0])
# No need to explicitly close connections using SQLAlchemy; it's handled automatically

# dfs contains all your DataFrames
