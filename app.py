import requests
from peewee import *
from classes import Board, Categories, Products
from constants import CATEGORIES_ARRAY, INTRO_TEXT

intro = Board("Choisissez ce que vous voulez faire")

intro.display(INTRO_TEXT)

if intro.get_input("number") == str(0):
	# intro.list_datas(CATEGORIES_ARRAY)
	intro.display(CATEGORIES_ARRAY)
else:
	print("not 0")

answer = intro.get_input("category")

cat_foods = Products.select().where(Products.category == str(CATEGORIES_ARRAY[int(answer)])).limit(10)
cat_foods_length = Products.select().where(Products.category == str(CATEGORIES_ARRAY[int(answer)]))
length = len(cat_foods_length)
print(length)

# arr = intro.list_datas(cat_foods, True)
arr = intro.display(cat_foods , True)
selected_product = intro.get_input("product")

# product_description = Products.select().where(Products.product_name)
print(arr[int(selected_product)])
product_description = Products.select().where(Products.id == arr[int(selected_product)])
# print(product_description)
for i in product_description:
	print("{} de la marque {}".format(i.product_name, i.brands))
	print("description : {}".format(i.description))
	print("le code de ce produit est : {}".format(i.product_code))
	print("le score nutritionnnel de ce produit est : {}".format(i.nutriscore))
