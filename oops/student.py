class Student:
    name:str
    id:int
    age:int
    gender:str
    course:str
    contact:str
    address:str

    def __init__(self,id,name,gender,age,course,contact,address):
        self.id=id
        self.name=name
        self.gender=gender
        self.age=age
        self.course=course
        self.contact=contact
        self.address=address

    def display_Student(self):
        print(self.id,self.name,self.gender,self.age,self.course,self.contact,self.address)



# creating objects

Student_instance = Student(6565,"roshan","male",23,"python",7902572838,"mannur")
Student_instance.display_Student()

