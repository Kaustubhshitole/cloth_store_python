#Clothes Class Section
class Clothes:
    total_pieces=0
#Line 5-10: Constructor that has 4 private attribute used to initialize this  members
def __init__(self,price,material,numberofpieces,name):
    self.__price = price
    self.__mateerial= material
    self.__numberofpieces = numberofpieces
    self.__name = name
    Clothes.total_pieces +=numberofpieces
    # Line 12-13: function used to get the price of clothes
    def set_price(self,price):
        self.__price = price

    #Line 15-16: function used to get set the price of clothes
    def get_price(self):
        return self.__price
    
    #line 18-19 : fuction used to set the material of clothes (actually this fuction never used in tjids program)
    def set_material(self,matrial):
        self.__material=material

    # line 21-22 : function used to get the material of clothes
    def get_material(self):
        return self.__matrial
    
    #line 24-26: fuction used to add an extra number of pieces(you can decrease number by entering -ve number)
    self.__numbersofpieces += numberofpieces
    Clothes.total_pieces +=numberofpieces

    #Line 28 - 29:fuction used to get the number of pieces(remaining as buying function incustomer class decrease
    # the number of pieces in clothes class)
    def get_number_of_pieces(self):
        return self._numberofpieces
    
    #line 32-33: fuction used to get name of clothes
    def get_name(self):
        return self.__name