from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Tourist_attractions_in_the_United_States'
data = requests.get(url)

bs_html = BeautifulSoup(data.text, 'html.parser')

panda_table = pd.DataFrame(columns=['Attraction','Location','Visitors(million)'])

for row in bs_html.find_all('tbody')[0].find_all('tr'):
  column = row.find_all('td')
  if(column!=[]):
    attraction = column[0].text.strip('\n')
    location = column[1].text.strip('\n')
    visitors = str(int(float(column[2].text[:-4])))
    panda_table = panda_table._append({'Attraction': attraction,'Location':location,'Visitors(million)':visitors}, ignore_index=True)

print(panda_table)