'''This Program is created by Yatharth Jain'''

#importing User class from user module
from user import User

#create class Application
class Application:
    
    def __init__(self):
        self.productCode = 0
        self.productName = ""
        self.stock = 0
        self.salePrice = 0
        self.manufactureCost = 0
        self.monthlyProduction = 0

    # HelloMessage function
    def HelloMessage():
        print("Welcome to programming principles Sample Product Inventory")    
    #TakeUserInput function
    def takeUserInput(self):
        #Enter product code
        self.productCode =input("Please enter the Product Code: ")
        # enter product name
        self.productName =input("Please enter the Product Name: ")
        # enter current stock
        self.stock = input("Please Enter the current Stock: ")
        # enter product sale price
        self.salePrice = input("Please enter the Product Sale Price: ")
        # enter product manufacture cost
        self.manufactureCost = input("Please enter the Product Manufacture Cost: ")
        # enter monthly estimated production cost
        self.monthlyProduction = input("Please enter the monthly production: ")
        
    # displayUserInput function
    def displayUserInput():
        #print product code
        #print(productCode) 

        #print product name

        #print sale price

        # print manufacture cost

        # print monthly production

        #create a for loop for months
            #create an instance of User class, i.e customer 
            #month i:
                #manufactured
                #return customer.itemsSold
                #return customer.stocked