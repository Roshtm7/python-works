# def add_numbers(n1,n2,n3):
#     return n1+n2+n3
# print (add_numbers(100,200,300))

# def add_numbers(*args):
    # print (sum(args))                             *args = (argument tuple)
                                                #  **kwargs = (keyword arguments dictionary)

# add_numbers(10,20)
# add_numbers(10,20,30)
# add_numbers(10,20,30,40)
# add_numbers(10,20,30,40,50)

number = 10.5
print(isinstance(number,(int,float)))


# def get_person(*args):
#     print(args[0])
#     print(args[1])
# get_person("hari","tvm","kakkanad")

def get_person(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("w_place"))
get_person(name="hari",w_place="tvm",n_place="kakkanad")


def flat_list(*args):
    flat=[]
    for arg in args:
        if isinstance(arg,list):
            flat.extend(flat_list(*arg))
        else:
            flat.append(arg)
    return flat
print(flat_list((10,20,[00,200],[1000,[2000,3000]])))






