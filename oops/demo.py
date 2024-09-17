class employee:
    eid:int
    name:str
    age:int
    gender:str
    department:str


    def set_employee(self,id,name,gender,department):
        self.eid = id
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department

    def display_employee(self):
        print(self.name,self.id,self.department)

        
