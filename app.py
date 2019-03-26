from classes import Board
from models import Products, Substitutes
from constants import CATEGORIES_ARRAY, INTRO_TEXT
import random

# class instanciation
intro = Board()

# first display of console
intro.display(INTRO_TEXT, "Choisissez ce que vous voulez faire")


# Select a new food or browse your replaced food list
if intro.get_input("number") == str(1):
    intro.display(CATEGORIES_ARRAY, "Les categories sont :")
else:
    substitute_list = Products.select().join(Substitutes).where(Products.id == Substitutes.food_id) 
    intro.display(substitute_list, "Vos aliments dejà substitués sont : ", True)

# select a category
answer = "0"

if answer.isdigit() is False:
    print("Ce n'est pas un chiffre, veuillez selectionner un chiffre")
    answer = intro.get_input("category")
else:
    answer = intro.get_input("category")

# make db requests
cat_foods = Products.select().where(Products.category_id == int(answer), Products.nutriscore != 'a').limit(10)
cat_foods_substitute = Products.select().where(Products.category_id == int(answer), Products.nutriscore == 'a').limit(10)

# select randomly a substitute food
length = len(cat_foods_substitute)

substitute = random.randint(0, length)
sub_array = []

for i, v in enumerate(cat_foods_substitute):
    sub_array.append(v)

# start a loop on console display
loop = True

while loop:

    # display all products from selected category
    arr = intro.display(cat_foods, "Voici la liste des aliments de cette categorie :", True)

    # select a product
    selected_product = intro.get_input("product")

    product_description = Products.select().where(Products.id == arr[int(selected_product)])

    # display description of selected product
    # selection = intro.display_product(selected_product, arr)

    sel2 = intro.disp_args(*product_description)

    # ask for next action
    response = intro.get_input("option")

    if response == 'x':
        loop = False
    elif response == "s":  
        intro.display_product(substitute, sub_array, True)
        sub = Substitutes.create(product_code=sub_array[substitute].product_code, food_id=sub_array[substitute].id)
        loop = False
