#importing random module
import random

#create class User with parameters (self,stock,manufactured Units per month,manufactureCost and saleprice)
class User:

    #define init function
    def __init__(self,stock,manufacturedUnits,manufactureCost,salePrice):
        #creating attribute for stock
        self._stock = stock
        self._unitsManufactured = manufacturedUnits
        self._manufactureCost = manufactureCost
        self._salePrice = salePrice

        #defining value of itemsSold
        self.itemsSold = 100 + random.randint(-10,10)
        #creating variable totalItemsProduced
        self.totalItemsProduced = 0
        #creating variable totalItemsSold
        self.totalItemsSold = 0
    
    def updateValues(self):
        self._stock += self._unitsManufactured - self.itemsSold
        self.totalItemsProduced = (self._unitsManufactured*12) + self._stock
        self.totalItemsSold += self.itemsSold 
