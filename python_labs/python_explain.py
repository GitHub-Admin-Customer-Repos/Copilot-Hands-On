import os
import json
import requests
import pandas as pd
import random
import string
from datetime import datetime

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def process_data(data):
    df = pd.DataFrame(data)
    df['id'] = df['id'].apply(lambda x: x if pd.notnull(x) else random_string())
    df['timestamp'] = datetime.now().isoformat()
    df['description'] = df['description'].apply(lambda x: x if pd.notnull(x) else 'No description available')
    df['value'] = df['value'].apply(lambda x: x if pd.notnull(x) else random.randint(1, 100))
    return df

def save_to_file(data, filename):
    data.to_json(filename, orient='records', lines=True)

def load_from_file(filename):
    if os.path.exists(filename):
        return pd.read_json(filename, orient='records', lines=True)
    return pd.DataFrame()

def main():
    url = 'https://api.example.com/data'
    filename = 'data.json'

    # Fetch data from URL
    data = fetch_data(url)
    if data is None:
        print("Failed to fetch data")
        return

    # Process the fetched data
    processed_data = process_data(data)

    # Save processed data to file
    save_to_file(processed_data, filename)

    # Load data from file
    loaded_data = load_from_file(filename)

    # Print loaded data
    for index, row in loaded_data.iterrows():
        print(f"ID: {row['id']}, Name: {row['name']}, Timestamp: {row['timestamp']}")
        print(f"Description: {row['description']}, Value: {row['value']}")
        print('-' * 40)

if __name__ == "__main__":
    main()