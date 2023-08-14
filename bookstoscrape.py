from bs4 import BeautifulSoup
import requests
import json
from pymongo import MongoClient

url = 'http://books.toscrape.com/index.html'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')

bookshelf = soup.findAll(
    "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

print('Aviable books: ' + "\n")

data = []

for book in bookshelf:
    book_title = book.h3.a["title"]
    book_price = book.findAll("p", {"class": "price_color"})
    price = book_price[0].text.strip()
    print(book_title + " " + price + "\n")

    book_data = {
        "Title": book_title,
        "Price": price
    }

    data.append(book_data)

with open('books_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4,  ensure_ascii=False)

client = MongoClient(
    'mongodb+srv://nahu:1234@cluster0.jbknozz.mongodb.net/?retryWrites=true&w=majority')

db = client['data']
collection = db['books']

with open('books_data.json') as json_file:
    data = json.load(json_file)
    collection.insert_many(data)
