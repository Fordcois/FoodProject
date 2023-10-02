
class Order:
    def __init__(self):
        self.basket=[]
        self.Style_Dots='*'*47

    def return_basket(self):
        return self.basket
    
    def Nothing_has_been_Ordered(self):
        return len(self.basket)==0

    def add_to_basket(self,ItemDict):
        self.basket.append(ItemDict)

    def remove_from_basket(self,ItemDict):
        self.basket.remove(ItemDict)

    def get_price(self):
        Price="{:.2f}".format((sum ([x['Price'] for x in self.basket])))
        return Price
    
    def print_basket(self,title):
        print (self.Style_Dots)
        print(title.center(47,' '))
        print (self.Style_Dots)
        if len(self.basket) == 0:
            print('Nothing Currently in your Basket!'.center(47,' '))
        else:
            for x in self.basket:
                print (f'{x["Code"]} - {x["DishName"]}{"." *(33 -len (x["DishName"]))} £{x["Price"]}')
            print (self.Style_Dots)
            print(f'Order Total: £{self.get_price()}'.rjust(47,' '))  
            
    

