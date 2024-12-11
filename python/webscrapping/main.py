import requests
from bs4 import BeautifulSoup
responce= requests.get("https://news.ycombinator.com/news")

yc_web_page = responce.text

soup = BeautifulSoup(yc_web_page,"html.parser")

artical_texts =[]
article_link = []
article_tag = soup.find_all(name="span", class_ = "titleline")

for article in article_tag:
    for item in article_tag:
        item_f = item.text
        artical_texts.append(item_f)
        link_get = item.find("a")
        link = link_get.get("href")
        article_link.append(link)


artical_upvote = [score.get_text() for score in soup.find_all(name="span", class_ = "score")]


print(artical_texts)
print(article_link)
print(artical_upvote)