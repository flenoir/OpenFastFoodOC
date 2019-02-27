
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
