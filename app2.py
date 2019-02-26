import requests


# # response = requests.get("https://fr.openfoodfacts.org/categories.json").json()
# response = requests.get("https://fr.openfoodfacts.org/products/categories.json").json()

# for i in response['tags']:
#     print("Le nom de la catégorie est : {}".format(i['name']))


# response2 = requests.get("https://fr.openfoodfacts.org/products/categories?query=popcorn")
# response2 = requests.get("https://fr.openfoodfacts.org/categorie/lentilles-vertes-bio.json").json()
# response2 = requests.get("https://fr.openfoodfacts.org/categorie/lentilles/1.json").json()
response2 = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=petit-dejeuners&sort_by=unique_scans_n&page_size=100&axis_x=energy&axis_y=products_n&action=display&json=1").json()


# print(response2.json())

for i in response2['products']:
    print("Le nom du produit est {} de la marque {}".format(i['product_name_fr'],i['brands']))
    print("Le code du produit est {} et il a un score nutritionnel : {}".format(i['code'],i['nutrition_grades']))



# nom du produit : product_name_fr
# nom de la marque : brands
# descritpion : generic_name_fr
# url du produit : url
# code produit : code
# photo du produit : image_ingredients_url ou image_nutrition_small_url
# score nutritionnel du produit : nutrition_grades
