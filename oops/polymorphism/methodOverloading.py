class Operation:
    def perform_add(self,*args):
        total=0
        for arg in args:
            if isinstance(arg,(int,float)):
                total=total+arg
        return total


    def get_max_number(self,*args):
        return max(args)

    def perform_multiply(self,*args):
        return min(args)

math=Operation()
print(math.perform_add(10,20))
print(math.perform_add(10,20,20.5,"hello",True))

print(math.get_max_number(10,20))
print(math.perform_multiply(1,2))



