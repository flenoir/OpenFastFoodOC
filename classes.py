import peewee

# Connect to a MySQL database on network.
db = peewee.MySQLDatabase('foodstuff', user='root', password='', host='localhost', port=3306)


class Board:

    def __init__(self):
        pass
      
    def display(self, data, text, bool=False):
        print("------------------------------------------------------------------")
        print("                  Bienvenue sur Gluten Free Food Swap                         ")
        print("------------------------------------------------------------------")
        print("             {}                 ".format(text))
        print("                                                                  ")
        if bool is False:
            for i, v in enumerate(data):
                print("       {} - {}              ".format(i+1,v))
            print("                                                                  ")
            print("------------------------------------------------------------------")
            
        else:
            ids_array = []
            for index, value in enumerate(data):                
                print("{} - {} {} / {}".format(index, value.product_name, value.brands, value.quantity))
                ids_array.append(value.id)            
            print("                                                                  ")
            print("------------------------------------------------------------------")
            return ids_array
    
    def get_input(self, question):
        var = input('select a {} :'.format(question))      
        return var
            
    def display_product(self, selected_product, arr):
        product_description = Products.select().where(Products.id == arr[int(selected_product)])

        for i in product_description:
            print("{} de la marque {}".format(i.product_name, i.brands))
            print("description : {}".format(i.description))
            print("le code de ce produit est : {}".format(i.product_code))
            print("le score nutritionnnel de ce produit est : {}".format(i.nutriscore))
            print("Swap this product to a better one, press 's', return to products list, press 'r', and exit, press 'x'")
            return selected_product, arr


# We define a first class for categories
class Categories(peewee.Model):
    # We specify model fields
    id = peewee
    name = peewee.CharField(40)

    class Meta:
        database = db
        db_table = "category"


# We define a db model called Products
class Products(peewee.Model):
    # We specify the model fields
    product_name = peewee.CharField(100)
    brands = peewee.CharField(100, null=True)
    description = peewee.CharField(200, null=True)
    product_url = peewee.CharField(150, null=True)
    product_code = peewee.CharField(20, null=True)
    product_image = peewee.CharField(100, null=True)
    nutriscore = peewee.CharField(1, null=True)
    stores = peewee.CharField(150, null=True)
    quantity = peewee.CharField(40, null=True)
    category_id = peewee.ForeignKeyField(Categories, field="id", null=True)

    # we define the reference to the database and the database table name
    class Meta:
        database = db
        db_table = "products"

# We define a db model called Products
class Substitutes(peewee.Model):
    # We specify the model fields
    product_code = peewee.CharField(20, null=True)
    food_id = peewee.ForeignKeyField(Products, field="id", null=True)

    # we define the reference to the database and the database table name
    class Meta:
        database = db
        db_table = "substitutes"