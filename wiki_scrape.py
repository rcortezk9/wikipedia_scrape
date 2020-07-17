from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population'
table_id = 'wikitable'

response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')

population_table = soup.find('table', attrs={'class': table_id})

df = pd.read_html(str(population_table))

df[0].to_csv('wikiscrape.csv', index=False)