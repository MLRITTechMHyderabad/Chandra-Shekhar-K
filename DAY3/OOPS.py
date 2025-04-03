class MyCar:#pasacl case
    wheels=4
    def __init__(self,n,b,c,p): #self keywords points to current obejct...
        print("Instantiating object")
        self.name = n 
        self.brand = b 
        self.color = c 
        self.price = p 
    def start(self,key=False):
        if key:
            print("Starting ",self.name,self.brand)
        else:
            print("Insert KEY")

    def display(self):
        print(self.brand,self.color,self.price)
class Customer(MyCar):
    def __init__(self, c_name,age,loc,n,b,c,p):
        super().__init__(n,b,c,p)
        self.customer_name=c_name
        self.age=age
        self.location=loc

    def display(self):
        print(self.customer_name,self.age)

class ShowRoom(MyCar):
    def __init__(self, s_name,s_loc,manager,n,b,c,p):
        super().__init__(n,b,c,p)
        self.showroom_name=s_name
        self.showroom_location=s_loc
        self.manager=manager
    def ChangeManager(self,m):
        self.manager=m


thar=MyCar("THAR","Mahindra","RED",1000)
nano=MyCar("Nano","Tata","White",100)
#s1=ShowRoom("Mahindra_TG","HYD","BIRLA")

c1=Customer("John",32,"HYD","Thar","Mahindra","Red",1000)
c1.display()
thar.display()
print(c1.age)
print(c1.brand)
print(c1.customer_name)
#print(thar.brand)
nano.start(True)