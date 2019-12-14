import requests

print("User Name: ")
userName = input()

url = "https://codeforces.com/api/user.info?handles="
url += userName

result = requests.get(url)

result = result.json()

print("Current Rank: ")
print(result["result"][0]["rank"])
print("Max Rank: ")
print(result["result"][0]["maxRank"])
print("Current Rating: ")
print(result["result"][0]["rating"])
print("Max Rating: ")
print(result["result"][0]["maxRating"])
