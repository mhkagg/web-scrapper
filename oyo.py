import pandas as pd
import csv
from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.oyorooms.com/search/?checkin=11%2F12%2F2022&checkout=12%2F12%2F2022&city=Bhubaneswar&country=india&coupon=&filters%5Bcity_id%5D=87&guests=2&location=Bhubaneswar%2C%20Odisha%2C%20India&roomConfig%5B%5D=2&rooms=1&searchType=city&showSearchElements=false&sort=&sortOrder='

headers = { 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15", 
    }

page = requests.get(url, headers = headers)
soup = bs(page.content, "html.parser")
lists = soup.find_all('div', class_ = 'oyo-row oyo-row--no-spacing listingHotelDescription') 

with open('oyo/hotelData.csv', 'w', newline='', encoding='UTF8') as file:
    writer = csv.writer(file)
    header = ['Hotel Name', 'Location', 'Price', 'Rating']
    writer.writerow(header)

    for list in lists:
        hotel_name = list.find('h3', class_ = 'listingHotelDescription__hotelName d-textEllipsis').text
        location = list.find('span', class_ = 'u-line--clamp-2').text
        price = list.find('span', class_ = 'listingPrice__slashedPrice d-body-lg').text
        rating = list.find('div', class_ = 'hotelRating').text
        data = [hotel_name, location, price, rating]
        writer.writerow(data)
     

df = pd.read_csv('oyo/hotelData.csv')
