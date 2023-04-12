# In this exercise we will scrape data from an api where an api key is needed
# My api key is in my secretkeys folder on my local machine. For your own api key please sign up on https://apilayer.com/ and suscribe for the exchange rates api

import requests
import pandas as pd
from secretkeys import api_layer_key

# See ApiLayer Exchange Rates Docs for information about API endpoints

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=&base=EUR"

# Here we enter the header to send to the Exchange Rates endpoint

headers= {
  "apikey": api_layer_key
}

# Performing the GET request

response = requests.request("GET", url, headers=headers, data = {})

status_code = response.status_code
result = response.text
rates = (response.json()['rates'])

# We convert our response to json and grab only the rates object. Then we store that information in our pandas DataFrame

pd_rates_table = pd.DataFrame(columns=['Currency','Rates'])

for row in rates:
    currency = row
    rate = rates[row]
    pd_rates_table = pd_rates_table._append({'Currency': currency,
                                            'Rates': rate}, ignore_index=True)
    
# We must include explicitly tell our to_csv function that we do not want to include the index as a saved value in our csv file

rates_csv = pd_rates_table.to_csv(index=False)

# The following will create your own csv file in the same directory where this file is located 

with open('exchange_rates_1.csv','w') as file:
    file.write(rates_csv)
    