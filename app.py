from classes import Board, Products, Substitutes
from constants import CATEGORIES_ARRAY, INTRO_TEXT
import random

intro = Board("Choisissez ce que vous voulez faire")


intro.display(INTRO_TEXT)


# Select a new food or browse your replaced food list
if intro.get_input("number") == str(0):
    intro.display(CATEGORIES_ARRAY)
else:
    print("not 0")

# select a category
answer = "x"

while answer.isdigit() is False:
    print("This is not a number, please enter un number")
    answer = intro.get_input("category")

cat_foods = Products.select().where(Products.category_id == int(answer), Products.nutriscore != 'a').limit(10)
cat_foods_substitute = Products.select().where(Products.category_id == int(answer), Products.nutriscore == 'a').limit(10)


length = len(cat_foods_substitute)
print(length)

print(random.randint(0, length))

substitute = random.randint(0, length)
sub_array = []

for i, v in enumerate(cat_foods_substitute):
    sub_array.append(v)


loop = True

while loop:

    # display all products from selected category
    arr = intro.display(cat_foods, True)

    # select a product
    selected_product = intro.get_input("product")

    selection = intro.display_product(selected_product, arr)

    response = intro.get_input("option")

    if response == 'x':
        loop = False
    elif response == "s":
        print("----------------------------------------------------------------------------------------------")
        print("the substitution food  with a better nutriscore is : {} which has a nutriscore notation of '{}'".format(sub_array[substitute].product_name, sub_array[substitute].nutriscore))
        sub = Substitutes.create(product_code=sub_array[substitute].product_code, food_id=sub_array[substitute].id)
        loop = False
