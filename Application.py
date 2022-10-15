'''This Program is created by Yatharth Jain'''

#importing User class from user module
from product import Product

#create class Application
class Application:
    def __init__(self):
        self.productCode = 0
        self.productName = ""
        self.stock = 0
        self.salePrice = 0.0
        self.manufactureCost = 0.0
        self.monthlyProduction = 0
        self.netProfit = 0.0

    # HelloMessage function
    def helloMessage():
        print("\n Welcome to programming principles Sample Product Inventory")
    helloMessage()

    #TakeUserInput function
    def takeUserInput(self):
        try:
            #Enter product code
            self.productCode = int(input("Please enter the Product Code: "))
            # enter product name
            self.productName = input("Please enter the Product Name: ")
            # enter current stock
            self.stock = int(input("Please Enter the current Stock: "))
            # enter product sale price
            self.salePrice = float(input("Please enter the Product Sale Price: "))
            # enter product manufacture cost
            self.manufactureCost = float(input("Please enter the Product Manufacture Cost: "))
            # enter monthly estimated production cost
            self.monthlyProduction = int(input("Please enter the monthly production: "))
        except Exception:
            print("Invalid entry please run program again: ")
    
    # Display Message
    def breakMessage(self):
        print("\n *******Programming Principles Sample Stock Statement******* \n")

    # displayUserInput function
    def displayUserInput(self):
        product = Product(self.stock,self.monthlyProduction,self.manufactureCost,self.salePrice)
        #print product code
        print(f"Product Code: {self.productCode}")
        #print product name
        print(f"Product Name {self.productName}")

        #print sale price
        print(f"Sale Price: {self.salePrice} CAD")
        # print manufacture cost
        print(f"Manufacture Cost: {self.manufactureCost} CAD")
        # print monthly production
        print(f"Monthly Production: {self.monthlyProduction} units")
        #create a for loop for months

        for month in range(1,13):
            #create an instance of User class, i.e product 
            product.updateValues()
            #month i
            print(f"Month {month}:")
            #manufactured
            print(f"    Manufactured: {product.getMonthlyProduction()} units")
            #return product.itemsSold
            print(f"    Sold: {product.getItemsSold()} units")
            #return product.stocked
            print(f"    Stock: {product.getStock()} units")
            self.netProfit += (product.getItemsSold() * self.salePrice - self.monthlyProduction * self.manufactureCost)

        #net Profit or loss
        if (self.netProfit > 0):
            print(f"Net Profit: {self.netProfit} CAD")
        elif (self.netProfit <0):
            print(f"Net Loss: {(-1) * self.netProfit} CAD")
        else:
            print("No net profit or loss earned!")

object1 = Application()
object1.takeUserInput()
object1.breakMessage()
object1.displayUserInput()
