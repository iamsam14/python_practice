# Objective - Use web scraping to get cities and states

# For this practice I will be using some python libraries. You might already have access to these libraries but other may need to install the libraries used in this practice exercise. Run the following commands in the terminal to install the libraries needed for this program

# pip3 install bs4==4.10.0
# pip3 install requests
# pip3 install pandas

# Imported libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd

# Extracting Data via Web Scraping

# In this exercise https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States provides information about the USA and its capitals. In this we will scrape the data from the table "State Captials" and store it as a JSON file

# First we store the contents of the web page using the requests library

url = 'https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States'
web_data = requests.get(url).text

# Scrape the data

# Using the webpage and BeautifulSoup, we will load the data into a pandas dataframe. The dataframe will contain State, Capital, Population(Proper).

bs_html = BeautifulSoup(web_data, 'html.parser')

panda_table = pd.DataFrame(columns=['State','Capital','Population(Proper)'])

# Once you have the index of the table we want to scrape, we iterate though it until we have appended every state, capital their respective population to our empty dataframe.

for row in bs_html.find_all('tbody')[1].find_all('tr'):

  col = row.find_all('td')
  if(col != []):
    state = col[0].a.text
    capital = row.find_all('th')[0].text.strip('\n')
    population = col[3].text.strip('\n')
    panda_table = panda_table._append({'State': state, 'Capital': capital, 'Population(Proper)': population}, ignore_index=True)

# Now we load the dataframe into a json file after converting it into a json object

json_obj = panda_table.to_json()
with open('USA_States_and_Capitals.json', 'w') as file:
  file.write(json_obj)