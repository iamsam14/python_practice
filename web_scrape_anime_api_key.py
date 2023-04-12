import requests
import pandas as pd
import xml.etree.ElementTree as ET
from secretkeys import anidb_key, anidb_ver

url = 'http://api.anidb.net:9001/httpapi?request=anime&client={}&clientver={}&protover=1&request=main'.format(anidb_key,anidb_ver)

response = requests.request("GET", url)
tree = ET.fromstring(response.text)
anime_df = pd.DataFrame(columns=['Episode Count', 'Anime Title'])

for el in tree[0].findall('anime'):
  if(el.find('episodecount'))!=None:
    episode_count = (el.find('episodecount').text)
  else:
    episode_count = 'unknown'

  anime_title = el.find('title').text
  anime_df = anime_df._append({'Episode Count': episode_count, 'Anime Title': anime_title}, ignore_index=True)

print(anime_df)
