import requests
from bs4 import BeautifulSoup
import csv

# get html from site
url = "https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life"
response = requests.get(url)
headers = response.headers
body = response.text[:2000]

# drill down into html to grab desired info -- quotes and their "authors"
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.findAll("strong")

with open("star_wars_html.csv", "w") as csv_file:
  writer = csv.writer(csv_file)
  column_headings = ["QUOTE"]
  writer.writerow(column_headings)

  for quote in quotes:
    text_only_quote = quote.text.strip()
    if len(text_only_quote):
      writer.writerow([text_only_quote])   


