import requests
import json
from bs4 import BeautifulSoup

listD=[]
res = requests.get(
    'https://www.golfdigest.com/hot-list/golf-clubs/drivers')
txt = res.text
status = res.status_code

soup=BeautifulSoup(res.content, 'html.parser')
page_title = soup.title.text

for i in range(len(soup.select(".m-Card__m-Content__a-Title"))):
    txt=(soup.select('.m-Card__m-Content__a-Title')[i].text)
    word=txt.strip()
    listD.append(word)
# for i in listD:
#     print (i)
#
# print (listD)

with open("Data.json", 'w') as f:
    json.dump(listD,f)
