import requests
from models import Categories, Products, Substitutes
from constants import CATEGORIES_ARRAY
import peewee
import re

# Connect to a MySQL database on network.
db = peewee.MySQLDatabase('foodstuff', user='root', password='', host='localhost', port=3306)

# The tables are created from a model with create_table()
Categories.create_table()		 
Products.create_table()
Substitutes.create_table()


# populate the Category table
for item in CATEGORIES_ARRAY:
    item = Categories.create(name=item)
    item.save()


# get id and name from categories to populate products table
def fill_db_from_categories(cat):
    for index, value in enumerate(cat):

        temp_var = "var" + str(index)

        temp_var = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=labels&tag_contains_0=contains&tag_0=sans%20gluten&tagtype_1=categories&tag_contains_1=contains&tag_1={}&sort_by=unique_scans_n&page_size=100&axis_x=energy&axis_y=products_n&action=display&json=1".format(value)).json()
       
        for x, i in enumerate(temp_var['products']):

            single_brand = re.findall("^([^,]*)", str(i['brands']))
            try:
                x = Products.create(product_name=i['product_name_fr'], brands=str(single_brand), description=i['generic_name_fr'], product_url=i['url'] ,product_code=i['code'], product_image=i['image_ingredients_url'] , nutriscore=i['nutrition_grades'], stores=i['stores_tags'], quantity=i['quantity'], category_id=index+1)
                x.save()
            except KeyError as e:
                print(e)


fill_db_from_categories(CATEGORIES_ARRAY)
