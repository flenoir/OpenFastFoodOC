import requests
from peewee import *
from classes import Board

# Connect to a MySQL database on network.
db = MySQLDatabase('foodstuff', user='root', password='', host='localhost', port=3306)
						 
# select all elements on category table
categories = db.execute_sql("SELECT * from category;")



# # response = requests.get("https://fr.openfoodfacts.org/categories.json").json()
# response = requests.get("https://fr.openfoodfacts.org/products/categories.json").json()

# for i in response['tags']:
#     print("Le nom de la catégorie est : {}".format(i['name']))


# response2 = requests.get("https://fr.openfoodfacts.org/products/categories?query=popcorn")
# response2 = requests.get("https://fr.openfoodfacts.org/categorie/lentilles-vertes-bio.json").json()
## response2 = requests.get("https://fr.openfoodfacts.org/categorie/lentilles/1.json").json()

# print(response2.json())

# for i in response2['products']:
#     print("Le nom du produit est {} de la marque {}".format(i['product_name_fr'],i['brands']))
#     print("Le code du produit est {} et il a un score nutritionnel : {}".format(i['code'],i['nutrition_grades']))



# nom du produit : product_name_fr
# nom de la marque : brands
# descritpion : generic_name_fr
# url du produit : url
# code produit : code
# photo du produit : image_ingredients_url ou image_nutrition_small_url
# score nutritionnel du produit : nutrition_grades

# print("------------------------------------------------------------------")
# print("                  Bienvenue sur Food Swap                         ")
# print("------------------------------------------------------------------")
# print("             Choisissez ce que vous voulez faire                  ")
# print("                                                                  ")
# print("           1 - Selectionnez un aliment à remplacer                ")
# print("           2 - Consulter la liste de vos aliments remplacés       ")
# print("                                                                  ")
# print("------------------------------------------------------------------")

intro = Board("Choisissez ce que vous voulez faire", "1 - Selectionnez un aliment à remplacer", "2 - Consulter la liste de vos aliments remplacés" )

intro.display()


selected = input("=> ")
# print(selected)
if selected == str(1):
	for item in categories:
		print(item[0], item[1])
else:
	print("not 1")

answer = input("select category => ")
print(answer)