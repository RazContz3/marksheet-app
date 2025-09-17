import sqlite3
import pandas as pd
import glob
import os

# Path to SQLite database (update if your app uses a different path)
db_path = 'app/data/marks.db'

# Path to cleaned CSVs
data_dir = 'data/processed'

conn = sqlite3.connect(db_path)

for csv_file in glob.glob(os.path.join(data_dir, 'final_clean_*.csv')):
    table_name = os.path.splitext(os.path.basename(csv_file))[0]
    print(f'Importing {csv_file} as table {table_name}')
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.close()
print('All CSVs imported into database.')
