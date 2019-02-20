import requests

# # response = requests.get("https://fr.openfoodfacts.org/categories.json").json()
# response = requests.get("https://fr.openfoodfacts.org/products/categories.json").json()

# for i in response['tags']:
#     print("Le nom de la catégorie est : {}".format(i['name']))


# response2 = requests.get("https://fr.openfoodfacts.org/products/categories?query=popcorn")
response2 = requests.get("https://fr.openfoodfacts.org/categorie/lentilles-vertes-bio.json")

print(response2.json())

# https://fr.openfoodfacts.org/categorie/snacks.json