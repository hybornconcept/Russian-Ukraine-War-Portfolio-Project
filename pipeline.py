import pandas as pd
import requests
import io
import psycopg2
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# kobo credentials
kobo_username = os.getenv("KOBOTOOLBOX_USERNAME")
kobo_password = os.getenv("KOBOTOOLBOX_PASSWORD")
KOBO_CSV_URL = 'https://kf.kobotoolbox.org/api/v2/assets/a7UgQCCmQDJxoJWaTwMXhD/export-settings/esJrBU9SNVd3NbQNtYHFLTa/data.csv'

# postgres credentials
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DATABASE = os.getenv("PG_DATABASE")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")

# schema and table details
SCHEMA_NAME = "war_data"
TABLE_NAME = "russian_ukrain_conflict"

#step 1: fetch the data from kobo
print('fetching data from kobocollect...')
response = requests.get(KOBO_CSV_URL, auth=HTTPBasicAuth(kobo_username, kobo_password))

if response.status_code == 200:
    print(f"Data was fetched successfully. Status code: {response.status_code}")
    
    csv_data = io.StringIO(response.text)
    df = pd.read_csv(csv_data, sep=';', encoding='utf-8', on_bad_lines='skip')

    # step 2: clean and transform data
    print('Processing data...')
    
    # compute total casualties using exact column names
    df['Total_soldiers_casualties'] = df[["Casualties", "Injured", "Captured"]].sum(axis=1)

    #step 3: Upload to Postgres
    print('Uploading data to Postgres...')
    conn = psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        database=PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD
    )
    cursor = conn.cursor()

    # Create the schema if it doesn't exist
    cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME};")

    # Drop and Recreate the table with exact column names
    cursor.execute(f"DROP TABLE IF EXISTS {SCHEMA_NAME}.{TABLE_NAME};")
    cursor.execute(f"""
        CREATE TABLE {SCHEMA_NAME}.{TABLE_NAME} (
            id SERIAL PRIMARY KEY,
            "start" TIMESTAMP,
            "end" TIMESTAMP,
            "Enter a date" DATE,
            "Country" TEXT,
            "Event" TEXT,
            "Oblast" TEXT,
            "Casualties" INTEGER,
            "Injured" INTEGER,
            "Captured" INTEGER,
            "Civilian Casualties" INTEGER,
            "New Recruits" INTEGER,
            "Combat Intensity" FLOAT,
            "Territory Status" TEXT,
            "Percentage Occupied" FLOAT,
            "Area Occupied" FLOAT,
            "Total_soldiers_casualties" INTEGER
        );
    """)

    # insert data into the table
    insert_query =f"""
        INSERT INTO {SCHEMA_NAME}.{TABLE_NAME} (
            "start", "end", "Enter a date", "Country", "Event", "Oblast", 
            "Casualties", "Injured", "Captured", "Civilian Casualties", 
            "New Recruits", "Combat Intensity", "Territory Status", 
            "Percentage Occupied", "Area Occupied", "Total_soldiers_casualties"
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
    """

    for _, row in df.iterrows():
        cursor.execute(insert_query,(
            row.get("start"),
            row.get("end"), 
            row.get("Enter a date"),
            row.get("Country"),
            row.get("Event"),
            row.get("Oblast"),
            row.get("Casualties", 0),
            row.get("Injured", 0),
            row.get("Captured", 0),
            row.get("Civilian Casualties", 0),
            row.get("New Recruits", 0),
            row.get("Combat Intensity", 0),
            row.get("Territory Status"),
            row.get("Percentage Occupied", 0),
            row.get("Area Occupied", 0),
            row.get("Total_soldiers_casualties", 0)
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print('Data successfully loaded into PostgreSQL')

else:
    print(f'Failed to fetch data. status code {response.status_code}')
