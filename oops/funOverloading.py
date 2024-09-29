# def add_numbers(n1,n2,n3):
#     return n1+n2+n3
# print (add_numbers(100,200,300))

def add_numbers(*args):
    print (sum(args))

add_numbers(10,20)
add_numbers(10,20,30)
add_numbers(10,20,30,40)
add_numbers(10,20,30,40,50)