from abc import ABC,abstractmethod

class Chai(ABC):
    def __init__(self,n,price,stock):
        self.name=n
        self.base_price=price
        self.stock=stock

    @abstractmethod
    def calculate_price():
        pass
    @abstractmethod
    def display_info():
        pass

class MasalaChai(Chai):
    def __init__(self, n, price, stock):
        super().__init__(n, price,stock)
        self.spice_cost=10
        print(self.name," ",self.base_price," ",self.stock)
    def calculate_price(self,base_price,spice_cost):
        price=spice_cost+base_price
        print(price)
    def display_info(self):
        print(self.name,"price per cup:",self.calculate_price(self.base_price),"Stock:",self.stock)
class GingerChai(Chai):
    def __init__(self, n, price, stock):
        super().__init__(n, price, stock)
        gingercost=8
        print(self.name," ",self.base_price," ",self.stock)
    def calculate_price(self,base_price,ginger_cost):
        price=self.base_price +ginger_cost
        print(price)
    def display_info(self):
        print(self.name,"price per cup:",self.calculate_price(self.base_price),"Stock:",self.stock)
        
class ElaichiChai(Chai):
    def __init__(self, n, price, stock):
        super().__init__(n, price, stock)
        elaichicost=12
        print(self.name," ",self.base_price," ",self.stock)
    def calculate_price(self,base_price,elaichicost):
        price= self.base_price + elaichicost
        print(price)
        
    def display_info(self):
        print(self.name,"price per cup:",self.calculate_price(self.base_price),"Stock:",self.stock)

class ChaiInventory():

    def add_chai(self):
        pass
    def show_inventory(self):
        pass
    def get_total_inventory_value():
        pass


chai1=MasalaChai("Masala Chai",20,50)
chai2=GingerChai("GingerChai",18,40)
chai3=ElaichiChai("Elaichi Chai",25,30)

