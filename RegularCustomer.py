#RegularCustomer Class Section
#Line 3-4 : used to  import classes from
from Customer import Customer
from Clothes import Clothes
class RegularCustomer(Customer):
    #Line 7-14 : function used to buy clothes and subtract the price of the clothes from customer money
    def buy_clothes(self,clothe):
            if(self.get_money() >= Clothes.get_price(clothe)):
             self.set_money(self.get_money()-Clothes.get_price(clothe))   
             remaining_pieces =Clothes.get_number_of_(clothe) -1
             Clothes.set_number_of_pieces(clothe,remaining_pieces)
             self.set_shoppingList(clothe)
             print("Thank you for your purchase")
            else:
               print("Sorry but you don't have enough money")
