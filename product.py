#importing random module
import random

#create class User with parameters (self,stock,manufactured Units per month,manufactureCost and saleprice)
class Product:

    #define init function
    def __init__(self,stock,manufacturedUnits,manufactureCost,salePrice):
        #creating attribute for stock
        self._stock = stock
        self._unitsManufactured = manufacturedUnits
        self._manufactureCost = manufactureCost
        self._salePrice = salePrice
        self.itemsSold = 100 + random.randint(-10,10)

    def updateValues(self):
        self.itemsSold = 100 + random.randint(-10,10)
        self._stock += self.getMonthlyProduction() - self.getItemsSold()

    
    #defining the accessors and mutators
    def setStock(self,stock):
        self._stock = stock

    def getStock(self):
        return self._stock

    def setMonthlyProdcution(self,manufacturedUnits):
        self._unitsManufactured = manufacturedUnits
    
    def getMonthlyProduction(self):
        return self._unitsManufactured

    def setItemsSold(self,itemsSold):
        self.itemsSold = itemsSold

    def getItemsSold(self):
        return self.itemsSold

