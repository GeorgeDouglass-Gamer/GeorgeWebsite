import requests
import json
from bs4 import BeautifulSoup

classtopull=".m-Card__m-Content__a-Title"
websiteURL='https://www.golfdigest.com/hot-list/golf-clubs/drivers'
jsonfile="DriverNames.json"
duplicate=[]
webList=[]
NewList=[]
res = requests.get(websiteURL)
txt = res.text
status = res.status_code

soup=BeautifulSoup(res.content, 'html.parser')
page_title = soup.title.text

#scrapes website for data and puts it into list
for i in range(len(soup.select(classtopull))):
    txt=(soup.select(classtopull)[i].text)
    word=txt.strip()
    webList.append(word)
webList.pop()

#loads old json file and puts it into list FileData
with open(jsonfile, 'r') as f:
    FileData=json.load(f)

#adds old contents of the file to the new list
for j in FileData:
    NewList.append(j)

#make sure it doesn't put the same driver in twice and creates new list.
for j in webList:
    shouldIAdd=True
    for i in FileData:
        if j == i:
            shouldIAdd=False
    if shouldIAdd == True:
        NewList.append(j)

#puts new list into the json file
with open(jsonfile, 'w') as f:
    json.dump(NewList,f)
