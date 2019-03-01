import peewee

# Connect to a MySQL database on network.
db = peewee.MySQLDatabase('foodstuff', user='root', password='', host='localhost', port=3306)

class Board:

    def __init__(self,text1, text2, text3):
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3

    def display(self):
        print("------------------------------------------------------------------")
        print("                  Bienvenue sur Food Swap                         ")
        print("------------------------------------------------------------------")
        print("             {}                 ".format(self.text1))
        print("                                                                  ")
        print("           {}              ".format(self.text2))
        print("           {}      ".format(self.text3))
        print("                                                                  ")
        print("------------------------------------------------------------------")


# We define a first class for categories
class Categories(peewee.Model):
    # We specify model fields
    name = peewee.CharField(40)

    class Meta:
        database = db
        db_table = "category"


# We define a db model called Products
class Products(peewee.Model):
    # We specify the model fields
    product_name = peewee.CharField(100)
    brands = peewee.CharField(100, null=True)
    description = peewee.CharField(100, null=True)
    product_url = peewee.CharField(100, null=True)
    product_code = peewee.CharField(20, null=True)
    product_image = peewee.CharField(100, null=True)
    nutriscore = peewee.CharField(1, null=True)
    stores = peewee.CharField(150, null=True)
    category = peewee.CharField(30)

    # we define the reference to the database and the database table name
    class Meta:
        database = db
        db_table = "products"