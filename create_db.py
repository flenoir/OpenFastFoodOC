import requests
# from peewee import *
from classes import Board
import peewee

# Connect to a MySQL database on network.
db = peewee.MySQLDatabase('foodstuff', user='root', password='', host='localhost', port=3306)
						 


# We define a db model called Products
class Products(peewee.Model):
    # We specify the model fields
    product_name = peewee.CharField(40)
    brands = peewee.CharField(40, null=True)
    description = peewee.CharField(50, null=True)
    product_url = peewee.CharField(100, null=True)
    product_code = peewee.CharField(20, null=True)
    product_image = peewee.CharField(100, null=True)
    nutriscore = peewee.CharField(1, null=True)
    category = peewee.CharField(30)

    # we define the reference to the database and the database table name
    class Meta:
        database = db
        db_table = "products"

# The table is created from a model with create_table(
Products.create_table()

# # We create a new instance and save it
# product1 = Products.create(product_name='Poulain', brands='Nestlé')
# product1.save()

# nom du produit : product_name_fr VARCHAR(40)
# nom de la marque : brands VARCHAR(40)
# descritpion : generic_name_fr VARCHAR(50)
# url du produit : url VARCHAR(100)
# code produit : code VARCHAR (20)
# photo du produit : image_ingredients_url ou image_nutrition_small_url VARCHAR(100)
# score nutritionnel du produit : nutrition_grades VARCHAR(1)


# select all elements on category table
categories = db.execute_sql("SELECT * from category;")

# we get id and name from categories 
def select(cat):
    for item in cat:
        print(item[0],item[1])
        # return item[0],item[1]

        temp_var = "var" + str(item[0])

        temp_var = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&sort_by=unique_scans_n&page_size=100&axis_x=energy&axis_y=products_n&action=display&json=1".format(item[1])).json()

        for x, i in enumerate(temp_var['products']):
            try :
                x = Products.create(product_name=i['product_name_fr'], brands=i['brands'], description=i['generic_name_fr'], product_url=i['url'] ,product_code=i['code'], product_image=i['image_ingredients_url'] , nutriscore=i['nutrition_grades'], category=str(item[1]))
                x.save()
                # print("Le nom du produit est {} de la marque {}".format(i['product_name_fr'],i['brands']))
                # print("Le code du produit est {} et il a un score nutritionnel : {}".format(i['code'],i['nutrition_grades']))
            except:
                print("one item was not found")


# cat_value = select(categories)
select(categories)

# response2 = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=petit-dejeuners&sort_by=unique_scans_n&page_size=100&axis_x=energy&axis_y=products_n&action=display&json=1").json()


# # print(response2.json())

# for x, i in enumerate(response2['products']):
#     try :
#         x = Products.create(product_name=i['product_name_fr'], brands=i['brands'], description=i['generic_name_fr'], product_url=i['url'] ,product_code=i['code'], product_image=i['image_ingredients_url'] , nutriscore=i['nutrition_grades']  )
#         x.save()
#         # print("Le nom du produit est {} de la marque {}".format(i['product_name_fr'],i['brands']))
#         # print("Le code du produit est {} et il a un score nutritionnel : {}".format(i['code'],i['nutrition_grades']))
#     except:
#         print("one item was not found")