import requests
import json
from Book import Book
book_list = []
response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699")

items = response.json()['items']
dict1 = items[0]

info = dict1['volumeInfo']

description = ''
title = ''
author = ''
publisher = ''
publish_date = ''
average_rating = ''
num_ratings = ''

for key, value in info.items():
    if key == 'description':
        description = value
    if key == 'title':
        title = value
    if key == 'authors':
        author = value[0]
    if key == 'publisher':
        publisher = value
    if key == 'publishedDate':
        publish_date = value
    if key == 'averageRating':
        average_rating = value
    if key == 'ratingsCount':
        num_ratings = value

new_book_1 = Book(author, title, publisher, publish_date, average_rating, num_ratings, description)
book_list.append(new_book_1)
print(new_book_1.__str__())

response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:1632158884")

items = response.json()['items']
dict1 = items[0]

info = dict1['volumeInfo']

description = ''
title = ''
author = ''
publisher = ''
publish_date = ''
average_rating = ''
num_ratings = ''

for key, value in info.items():
    if key == 'description':
        description = value
    if key == 'title':
        title = value
    if key == 'authors':
        author = value[0]
    if key == 'publisher':
        publisher = value
    if key == 'publishedDate':
        publish_date = value
    if key == 'averageRating':
        average_rating = value
    if key == 'ratingsCount':
        num_ratings = value

new_book_2 = Book(author, title, publisher, publish_date, average_rating, num_ratings, description)
book_list.append(new_book_2)

response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:0441013597")

items = response.json()['items']
dict1 = items[0]

info = dict1['volumeInfo']

description = ''
title = ''
author = ''
publisher = ''
publish_date = ''
average_rating = ''
num_ratings = ''

for key, value in info.items():
    if key == 'description':
        description = value
    if key == 'title':
        title = value
    if key == 'authors':
        author = value[0]
    if key == 'publisher':
        publisher = value
    if key == 'publishedDate':
        publish_date = value
    if key == 'averageRating':
        average_rating = value
    if key == 'ratingsCount':
        num_ratings = value

new_book_3 = Book(author, title, publisher, publish_date, average_rating, num_ratings, description)
book_list.append(new_book_3)

with open("bookData.csv", "w") as file:
    for book in book_list:
        file.write(book.__str__())
