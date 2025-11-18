import requests
import numpy as np

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return []

def process_data(data):
    # Extract the first 10 titles and process with numpy
    titles = [item['title'] for item in data[:10]]
    lengths = np.array([len(title) for title in titles])
    return titles, lengths

def main():
    print("Fetching data...")
    data = fetch_data()
    if data:
        titles, lengths = process_data(data)
        print("\nTitles of first 10 posts:")
        for title in titles:
            print(f"- {title}")
        print("\nLengths of titles:")
        print(lengths)

if __name__ == "__main__":
    main()
