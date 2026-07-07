import requests

response = requests.get("https://api.github.com/users/xyzabc123fakeuser")

data = response.json()


if response.status_code == 200:
    print(f"User: {data['name']}")
    print(f"Followers: {data['followers']}")
    print(f"Public Repos: {data['public_repos']}")
else:
    print(f"Something went wrong: {response.status_code}")