import requests 


url = "https://jsonplaceholder.typicode.com/posts"


data = {
    "title": "My First Python POST",
    "body":"Hari sent this from Python Code",
    "userId": 1 
}

response = requests.post(url,json = data)

result = response.json()

if response.status_code == 201:
    print(f"Created successfully!")
    print(f"Post ID: {result['id']}")
    print(f"Title: {result['title']}")
else:
    print(f"Error: {response.status_code}")