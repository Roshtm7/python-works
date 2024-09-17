class Bike:
    name:str
    brand:str
    price:int

    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price

    def __str__(self):
        return self.name

class Showroom:
    name=str
    place=str
    bikes=list

    def __init__(self,name,place):
        self.name=name
        self.place=place
        self.bikes=[]

    def add_vehicle(self,bike):
        self.bikes.append(bike)

    def list_vehicles(self):
        for b in self.bikes:
            print(b)


pulsar_instance=Bike("pulsar","bajaj",80000)
dominor_instance=Bike("dominor","bajaj",120000)
himalayan_instance=Bike("himalayan","re",200000)
hunk_instance=Bike("hunk","hero",50000)

showroom_instance=Showroom("popular","kakkanad")

showroom_instance.add_vehicle(pulsar_instance)
showroom_instance.add_vehicle(dominor_instance)
showroom_instance.add_vehicle(himalayan_instance)
showroom_instance.add_vehicle(hunk_instance)
showroom_instance.list_vehicles()

showroom_instance2=Showroom("tags","thrissur")
showroom_instance2.add_vehicle(himalayan_instance)
showroom_instance2.add_vehicle(hunk_instance)
showroom_instance2.add_vehicle(dominor_instance)
showroom_instance2.list_vehicles()
