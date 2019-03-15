import peewee
# from constants import CATEGORIES_ARRAY

# Connect to a MySQL database on network.
db = peewee.MySQLDatabase('foodstuff', user='root', password='', host='localhost', port=3306)

class Board:

    def __init__(self,text1):
        self.text1 = text1
      

    def display(self, data, bool=False):
        print("------------------------------------------------------------------")
        print("                  Bienvenue sur Food Swap                         ")
        print("------------------------------------------------------------------")
        print("             {}                 ".format(self.text1))
        print("                                                                  ")
        if bool == False:
            for i,v in enumerate(data):
                print("       {} - {}              ".format(i,v))
            print("                                                                  ")
            print("------------------------------------------------------------------")
            
        else:
            ids_array =[]
            for index, value in enumerate(data):
                print("{} - {} and id is {} ".format(index, value.product_name, value.id))
                ids_array.append(value.id)
            # print(ids_array)
            # return ids_array
            print("                                                                  ")
            print("------------------------------------------------------------------")
            return ids_array
    
    def get_input(self, question):
        var = input('select a {} :'.format(question))
        return var

    # def list_datas(self, datas, bool=False):
    #     if bool == False:
    #         for index, value in enumerate(datas):
    #             print("{} - {} ".format(index, value))
    #     else:
    #         ids_array =[]
    #         for index, value in enumerate(datas):
    #             print("{} - {} and id is {} ".format(index, value.product_name, value.id))
    #             ids_array.append(value.id)
    #         # print(ids_array)
    #         return ids_array


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
    description = peewee.CharField(200, null=True)
    product_url = peewee.CharField(150, null=True)
    product_code = peewee.CharField(20, null=True)
    product_image = peewee.CharField(100, null=True)
    nutriscore = peewee.CharField(1, null=True)
    stores = peewee.CharField(150, null=True)
    category = peewee.CharField(30)

    # we define the reference to the database and the database table name
    class Meta:
        database = db
        db_table = "products"