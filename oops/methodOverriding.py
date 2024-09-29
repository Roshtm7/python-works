class Parent:
    def bike(self):
        print("glamour")

    def mobile(self):
        print("apple")

class Child(Parent):
    def mobile(self):
        print("samsung")

    def bike(self):
        print("bullet")
child_instance=Child()
child_instance.bike()
child_instance.mobile()


