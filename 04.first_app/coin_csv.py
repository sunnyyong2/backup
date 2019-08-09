import csv
import requests
from bs4 import BeautifulSoup

# url = "https://www.bithumb.com/"
# response = requests.get(url).text
# soup = BeautifulSoup(response, "html.parser")

# tr = soup.select("#tableAsset > tbody > tr")

# with open("bit_coin.csv", 'w', encoding = 'utf-8', newline = "") as f:
#     csv_writer = csv.writer(f)
#     for r in tr :
#         print(r.select_one('.blind').text)
#         print(r.select_one('.sort_real').text)
#         row = [r.select_one('.blind').text.strip(), r.select_one('.sort_real').text]
#         csv_writer.writerow(row)

url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1d"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")

tr = soup.select("#content > div.NE\=a\:t1a > div._tracklist_mytrack.tracklist_table.tracklist_type1 > table > tbody > tr > td")
print(tr)
for r in tr:
    if r.select_one('.ellipsis') != None:
        print(r.select_one('.ellipsis').text.strip())
    ranking = r.select('.ranking > span')
    if ranking != None:
        for rank in ranking:
            print(rank.text)
        
          

# with open("bit_coin.csv", 'w', encoding = 'utf-8', newline = "") as f:
#     csv_writer = csv.writer(f)
#     for r in tr :
#         print(r.select_one('.blind').text)
#         print(r.select_one('.sort_real').text)
#         row = [r.select_one('.blind').text.strip(), r.select_one('.sort_real').text]
#         csv_writer.writerow(row)