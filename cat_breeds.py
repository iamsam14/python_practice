from bs4 import BeautifulSoup
import pandas as pd
import requests
import html5lib
import re

url = 'https://en.wikipedia.org/wiki/List_of_cat_breeds'
html_data = requests.get(url)

bs_html = BeautifulSoup(html_data.text, 'html.parser')

panda_table = pd.DataFrame(columns=['Breed','Body Type','Coat Pattern'])

for row in bs_html.find_all('tbody')[0].find_all('tr'):

  column = row.find_all('td')
  if(column != []):
    breed = row.find('th').text.strip('\n')
    if(re.search(r'\[|\(', breed)):
      breed = breed[:breed.rfind('(')] if breed.rfind('(') > 0 else breed[:breed.rfind('[')]
    body = column[2].text.strip('\n')
    coat = column[3].text
    panda_table = panda_table._append({'Breed': breed,'Body Type':body,'Coat Pattern':coat}, ignore_index=True)

print(panda_table)