import json
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

url = 'https://www.hardgamers.com.ar/search?text=3060+ti'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

store = soup.find_all('div', class_='col-12 col-lg-9')
print(store)

# data = []

# for gpu in store:
#     store_name = gpu.find_all('h4', class_='subtitle')
#     gpu_price = gpu.find_all(
#         "h2", attrs={"itemprop": "price", "class": "product-price"})

#     store_name_text = [name.get_text().replace(' ', '', 1)
#                        for name in store_name]
#     gpu_price_text = [price.get_text().replace(
#         ' ', '').replace('\n', '') for price in gpu_price]


# for store, price in zip(store_name_text, gpu_price_text):
#     print(store, price)

#     gpu_data = {'Store': store,
#                 'Price': price
#                 }
#     data.append(gpu_data)

# with open('buy_gpu.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)

# client = MongoClient(
#     'mongodb+srv://nahu:1234@cluster0.jbknozz.mongodb.net/?retryWrites=true&w=majority')

# db = client['data']
# collection = db['gpus']

# with open('buy_gpu.json') as json_file:
#     data = json.load(json_file)
#     collection.insert_many(data)
