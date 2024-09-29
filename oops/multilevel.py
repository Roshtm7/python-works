class Grandparent():
    def m1(self):
        print("Grandparent class m1 method")


class Parent():
    def m2(self):
        print("Parent class m2 method")

class Child():
    def m3(self):
        print("Child m3 method")

child_instance=Child()
child_instance.m3()
child_instance.m2()
child_instance.m1()
