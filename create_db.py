import requests
from classes import Board, Categories, Products
import peewee
import re

# Connect to a MySQL database on network.
db = peewee.MySQLDatabase('foodstuff', user='root', password='', host='localhost', port=3306)

# The table is created from a model with create_table()
Categories.create_table()				 

# The table is created from a model with create_table()
Products.create_table()

categories_array = ['petit-dejeuners', 'plats-prepares', 'snacks-sales', 'biscuits-et-gateaux', 'pizzas', 'produits-laitiers', 'epicerie', 'desserts', 'charcuteries', 'cereales-et-derives' ]                                            

# populate the Category table
for item in categories_array:
    item = Categories.create(name=item)
    item.save()

# # We create a new instance and save it
# product1 = Products.create(product_name='Poulain', brands='Nestlé')
# product1.save()

# we get id and name from categories 
def fill_db_from_categories(cat):
    for index, value in enumerate(cat):

        temp_var = "var" + str(index)

        temp_var = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=labels&tag_contains_0=contains&tag_0=sans%20gluten&tagtype_1=categories&tag_contains_1=contains&tag_1={}&sort_by=unique_scans_n&page_size=100&axis_x=energy&axis_y=products_n&action=display&json=1".format(value)).json()
		
		# temp_var = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&tagtype_0=labels&tag_contains_0=contains&tag_0=sans-gluten&tagtype_1=origins&tag_contains_1=contains&tag_1=france&sort_by=unique_scans_n&page_size=100&axis_x=energy&axis_y=products_n&action=display&json=1".format(value)).json()

        # for x, i in enumerate(temp_var['products']):
        #     try :
        #         x = Products.create(product_name=i['product_name_fr'], brands=i['brands'], description=i['generic_name_fr'], product_url=i['url'] ,product_code=i['code'], product_image=i['image_ingredients_url'] , nutriscore=i['nutrition_grades'], stores=i['stores_tags'], category=str(value))
        #         x.save()
        #     except:
        #         print("one item was not found")

       
        for x, i in enumerate(temp_var['products']):

            single_brand = re.findall("^([^,]*)", str(i['brands']))
            try :
                x = Products.create(product_name=i['product_name_fr'], brands=str(single_brand), description=i['generic_name_fr'], product_url=i['url'] ,product_code=i['code'], product_image=i['image_ingredients_url'] , nutriscore=i['nutrition_grades'], stores=i['stores_tags'], quantity=i['quantity'], category_id=index+1)
                x.save()
            # except:
            #     print("one item was not found")
            except KeyError as e:
                print(e)
                # print(i['code'])


fill_db_from_categories(categories_array)
