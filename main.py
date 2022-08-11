import bs4
import requests
from bs4 import BeautifulSoup
import re

HEADERS = {'Cookie': '_ym_uid=1650396073535463855; _ym_d=1650396073; hl=ru; fl=ru; _ga=GA1.2.1066111727.1650396077; visited_articles=349860:442800:322086:226521:580710:480838; _gid=GA1.2.2147445574.1659898053; habr_web_home_feed=/all/; _ym_isad=2',
          'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'java', 'api', 'excel'}

pattern = (r"\w+")

response = requests.get("https://habr.com/ru/all/", headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features = "html.parser")
articles = soup.findAll(class_ = "tm-article-snippet")
for article in articles:
    previews = article.find("div", "tm-article-body tm-article-snippet__lead").text
    words = set(re.findall(pattern, previews))
    if words & KEYWORDS:
        date = article.find("span", class_="tm-article-snippet__datetime-published").text
        name = article.find("h2","tm-article-snippet__title tm-article-snippet__title_h2").text
        link = "https://habr.com" + article.find("a", "tm-article-snippet__title-link").get("href")
        print(f"<{date}> - <{name}> - <{link}>")







