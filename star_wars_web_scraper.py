import requests
from bs4 import BeautifulSoup

# get html from site
url = "https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life"
response = requests.get(url)
headers = response.headers
body = response.text[:2000]

# drill down into html to grab desired info -- quotes and their "authors"
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.findAll("strong")
print(quotes)

