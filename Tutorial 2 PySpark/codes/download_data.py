import requests

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

response = requests.get(url)

with open("../data/countries.csv", "wb") as file:
    file.write(response.content)

print("Dataset downloaded successfully!")