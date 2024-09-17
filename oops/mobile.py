class Mobile:
    name:str
    storage:str
    brand:str
    price:int

    def __init__(self,name,storage,brand,price):
        self.name=name
        self.storage=storage
        self.brand=brand
        self.price=price

    def display_details(self):
        print(self.name,self.storage,self.brand,self.price)

#object creation



Mobile_instance = Mobile("iphone","128",576,"apple")
Mobile_instance.display_details()




