'''This Program is created by Yatharth Jain'''

#importing User class from user module
from calendar import month
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
        print("\n Welcome to programming principles Sample Product Inventory")    
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
    
    # Display Message
    print("\n *******Programming Principles Sample Stock Statement******* \n")

    # displayUserInput function
    def displayUserInput(self):
        #print product code
        print(f"Product Code: {self.productCode}")
        #print product name
        print(f"Product Name {self.productName}")

        #print sale price
        print(f"Sale Price: {self.salePrice}")
        # print manufacture cost
        print(f"Manufacture Cost: {self.manufactureCost}")
        # print monthly production
        print(f"Monthly Production: {self.monthlyProduction}")
        #create a for loop for months
        months = 1
        while(months<=12):
            #create an instance of User class, i.e customer 
            customer = User(self.stock,self.monthlyProduction,self.manufactureCost,self.salePrice)
            #month i
            print(f"Month {months}:")
            #manufactured
            print(f"Manufactured: {customer._unitsManufactured}")
            #return customer.itemsSold
            print(f"Sold: {customer.itemsSold}")
            #return customer.stocked
            print(f"Stock: {customer._stock}")
            months += 1