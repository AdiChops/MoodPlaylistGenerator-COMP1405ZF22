import requests
from bs4 import BeautifulSoup

URL = "https://youtube.com/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("h3", class_="yt-lockup-title")

print(results)