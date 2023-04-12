import pandas as pd
from datetime import datetime
import wget

url = 'https://www.stats.govt.nz/assets/Uploads/Consumers-price-index/Consumers-price-index-December-2022-quarter/Download-data/Consumers-price-index-December-2022-quarter-Infoshare-data.csv'
csv_file = wget.download(url)
print('\n')

def extract():
  read_csv = pd.read_csv('Consumers-price-index-December-2022-quarter-Infoshare-data.csv', encoding='unicode_escape')
  return read_csv

def transform(data):
  transformed_data = data
  transformed_data.rename(index=str, columns={'Data _Value': 'Data_Value'}, inplace=True)
  transformed_data = transformed_data[['Data_Value', 'Type', 'Description']]
  return transformed_data

def load(target_file, data_to_load):
  data_to_load.to_csv(target_file)

def log(message):
  timestamp_format = '%Y-%h-%d-%H:%M:%S'
  now = datetime.now()
  timestamp = now.strftime(timestamp_format)
  with open('logfile.txt','a') as f:
    f.write(timestamp + ', ' + message + '\n')

log('ETL Job Started')
log('Extract phase Started')
extracted_data = extract()
log('Extract phace Ended')

log('Transform phase started')
transformed_data = transform(extracted_data)
log('Transform phase Ended')

log('Load phase Started')
load('consumer_price_info.csv', transformed_data)
log('Load phase Ended')

print(transform(extracted_data))
