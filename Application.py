'''This Program is created by Yatharth Jain'''

#importing User class from user module
from user import User

#create class Application
class Application:

    # HelloMessage function
    def HelloMessage():
        print("Welcome to programming principles Sample Product Inventory")    
    #TakeUserInput function
    def takeUserInput():
        #Enter product code
        productCode =input("Please enter the Product Code: ")
        # enter product name
        productName =input("Please enter the Product Name: ")
        # enter current stock
        stock = input("Please Enter the current Stock: ")
        # enter product sale price
        salePrice = input("Please enter the Product Sale Price: ")
        # enter product manufacture cost
        manufactureCost = input("Please enter the Product Manufacture Cost: ")
        # enter monthly estimated production cost
        monthlyProduction = input("Please enter the monthly production: ")

    # displayUserInput()
        
        #print product code 

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