import requests

def get_data():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"  # Replace with your API endpoint
    response = requests.get(url)
    
    if response.status_code == 200:
        # .json() automatically parses the JSON from the response
        data = response.json()
        print("Data retrieved successfully!")
        print(data)
        print(data["abilities"][0]["ability"]["name"])
    else:
        print(f"Error fetching data. Status code: {response.status_code}")

if __name__ == "__main__":
    get_data()
