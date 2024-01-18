import pandas as pd
import csv
from bs4 import BeautifulSoup as bs
import requests

session = requests.Session()
url = 'URL_login' # replace url with the url for login

resp = session.get(url)
soup= bs(resp.text,'html.parser')

if resp.status_code == 200:
    csrf_token = soup.find("input",{"name":"authenticity_token"}).get("value")
    timestamp = soup.find("input",{"name":"timestamp"}).get("value")
    timestamp_secret = soup.find("input",{"name":"timestamp_secret"}).get("value")
else:
    print(f'Authentication failed. Status code: {resp.status_code}')

# replace USERNAME and PASSWORD with the url and password
payload={"login":"USERNAME","password":"PASSWORD","authenticity_token":csrf_token,"timestamp":timestamp,"timestamp_secret":timestamp_secret}
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36","Content-Type":"application/x-www-form-urlencoded"}

# replace URL with the url of page after login in
resp = session.post('URL', data=payload, headers=head)
print(resp.status_code)

if resp.status_code == 200:
    # replace URL with the url for scarpping
    url = 'URL'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",}
    page = requests.get(url, headers = headers)
    soup = bs(page.content, "html.parser")
    lists = soup.find_all('div', {"class":"col-10 col-lg-9 d-inline-block"}) 

    with open('file.csv', 'w', newline='', encoding='UTF8') as file:
        writer = csv.writer(file)
        header = ['name', 'message']
        writer.writerow(header)

        for list in lists:
            name = list.find('a')
            if name:
                name = name.text.strip()
            else:
                name = "NA"
            
            message = list.find('p', {"itemprop": "description"})
            if message:
                message = message.text.strip()
            else:
                message = "NA"
            data = [name, message]
            writer.writerow(data)
    
    df = pd.read_csv('file.csv')

else:
    print("error")