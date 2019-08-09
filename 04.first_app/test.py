import requests
from bs4 import BeautifulSoup
url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%9D%A0%EB%B3%84%20%EC%9A%B4%EC%84%B8"
res = requests.get(url).text
soup = BeautifulSoup(res, "html.parser")
ls = soup.select("#main_pack > div.content_search.section > div > div.contents03_sub > div")
print(ls)