import requests

url = "https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life"
response = requests.get(url)

headers = response.headers
body = response.text[:2000]

print(body)

