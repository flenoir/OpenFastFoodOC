import peewee

# Connect to a MySQL database on network.
db = peewee.MySQLDatabase('foodstuff', user='root', password='', host='localhost', port=3306)

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