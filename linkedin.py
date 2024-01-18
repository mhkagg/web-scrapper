import pandas as pd
import csv
from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3758400695'

headers = { 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15", 
    }

page = requests.get(url, headers = headers)
soup = bs(page.content, "html.parser")
lists = soup.find('div') 
print(lists)
