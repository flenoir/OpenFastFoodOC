from models import Products, Substitutes

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
            
    def display_product(self, selected_product, arr, bool=False):
        product_description = Products.select().where(Products.id == arr[int(selected_product)])

        for i in product_description:
            print("#########################################################")
            print("{} de la marque {}".format(i.product_name, i.brands))
            print("---------------------------------------------------------")
            print("description : {}".format(i.description))
            print("le code de ce produit est : {}".format(i.product_code))
            print("le score nutritionnnel de ce produit est : {}".format(i.nutriscore))
            print("Vous pouvez trouver ce produit dans les magasins {}".format(i.stores))
            print("l'url de ce produit est {}".format(i.product_url))
            print("#########################################################")
            if bool is False:
                print("Pour substituer ce produit, tapez 's', retourner à la liste des produits, tapez 'r', et pour sortir, tapez 'x'")
            return selected_product, arr

    def disp_args(self, *args):

        for i in args:
            print("#########################################################")
            print("{} de la marque {}".format(i.product_name, i.brands))
            print("---------------------------------------------------------")
            print("description : {}".format(i.description))
            print("le code de ce produit est : {}".format(i.product_code))
            print("le score nutritionnnel de ce produit est : {}".format(i.nutriscore))
            print("Vous pouvez trouver ce produit dans les magasins {}".format(i.stores))
            print("l'url de ce produit est {}".format(i.product_url))
            print("#########################################################")
            if bool is False:
                print("Pour substituer ce produit, tapez 's', retourner à la liste des produits, tapez 'r', et pour sortir, tapez 'x'")
            # return args