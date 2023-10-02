from OrderClass import *
from twillio import *
from datetime import datetime, timedelta

class restaurant:
    def __init__(self):
        self.Style_Dots='*'*47
        self.Dishes=[{'DishName':'Margherita','Price':10.99,'Code':'MARG'}, 
                    {'DishName':'Pepperoni','Price':11.99,'Code':'PEPP'},
                    {'DishName':'Volcano','Price':12.49,'Code':'VOLC'},
                    {'DishName':'Garden Special','Price':10.99,'Code':'GARD'},
                    {'DishName':'Mushroom','Price':12.99,'Code':'MUSH'},
                    {'DishName':'Ham & Pineapple','Price':12.50,'Code':'PINE'},
                    {'DishName':'All the Meats','Price':14.00,'Code':'MEAT'},
                    ]
        self.MealCodes=[x['Code'] for x in self.Dishes]
        self.basket=[]
        self.order=Order()

    def remove_item_from_basket(self):
        print ("- Enter 'BACK' if you do not wish to remove anything")
        Selected_Item=input('INPUT: ').upper()
        if Selected_Item =='BACK':
            print ("Returning to Ordering Menu...")
            self.Place_Order()
        elif Selected_Item in self.MealCodes:
            for MenuDictEntry in self.Dishes:
                if (MenuDictEntry['Code']==Selected_Item ):
                    if (MenuDictEntry in self.order.return_basket()):
                        self.order.remove_from_basket(MenuDictEntry)
                        print (f'One {MenuDictEntry["DishName"]} removed from your Basket!')
                        self.order.print_basket('Basket')
                    else:
                        print (f'No {MenuDictEntry["DishName"]} found in your Basket!')
                        print ("Returning to Ordering Menu...")
        else:
            print (f' "{Selected_Item}" is not a valid code - Try Again or write "BACK" to Return to order page..' )
            self.remove_item_from_basket()

    def print_menu(self):
        print (self.Style_Dots)
        print('MENU'.center(47,' '))
        print (self.Style_Dots)
        for x in self.Dishes:
            print (f'{x["Code"]} - {x["DishName"]}{"." *(33 -len (x["DishName"]))} £{"{:.2f}".format(x["Price"])}')

    def Place_Order(self):
        Still_Ordering=True

        while Still_Ordering==True:
            print(self.Style_Dots)
            print(' - Input the 4 letter code to ADD item to your basket')
            print (" - Enter 'DONE' when you're finished")
            print (" - Enter 'REMO' to remove something from the menu")
            print (" - Enter 'MENU' to view the Menu")
            
            item_Being_Ordered=input('INPUT: ').upper()
            
            if item_Being_Ordered =='DONE':
                Still_Ordering=False

            elif item_Being_Ordered =='MENU':
                self.print_menu()

            elif item_Being_Ordered=='REMO':
                self.remove_item_from_basket()

            elif item_Being_Ordered.upper() in self.MealCodes:
                for MenuDictEntry in self.Dishes:
                    if MenuDictEntry['Code']==item_Being_Ordered:
                        print (self.Style_Dots)
                        self.order.add_to_basket(MenuDictEntry)
                        print (f'One {MenuDictEntry["DishName"]} added to your Basket!')
                        print ('Your Basket is currently:')
                        self.order.print_basket('Basket')
                        
            else:
                print(self.Style_Dots)
                print (f" '{item_Being_Ordered}' is not a valid code, Please try again or enter 'DONE' when you are finished" )

        if self.order.Nothing_has_been_Ordered():
            print('Thanks for Visiting'.center(47,' '))
            print('Hope to See you Again Soon'.center(47,' '))
        
        else:        
            How_Many_Minutes_To_Deliver=30
            Expected_DeliveryTime = (datetime.now()+timedelta(minutes= How_Many_Minutes_To_Deliver)).strftime("%H:%M")
            print ('Order Confirmed! - You Will Recieve a confirmation text order shortly')
            self.order.print_basket('Customer Reciept')
            print ("Enter Your Phone Number (including Country code) to Recieve text updates about your order")
            PhoneNumber=input('Enter Phone Number:')
            send_twillio_message(PhoneNumber,f'Thank you! Your order was placed and will be delivered before {Expected_DeliveryTime}')
            print (f'Confirmation Message sent to {PhoneNumber}')
