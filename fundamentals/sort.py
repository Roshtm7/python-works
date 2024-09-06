#read 3 numbers from user num1,num2,num3
#print these 3 numbers in sorted order

num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))
if(num1<=num2<=num3):
    sorted_order = [num1,num2,num3]
elif(num1<=num3<=num2):
    sorted_order = [num1,num3,num2]
elif(num2<=num1<=num3):
    sorted_order = [num2,num1,num3]
elif(num2<=num3<=num1):
    sorted_order = [num2,num3,num1]
elif(num3<=num1<=num2):
    sorted_order = [num3,num1,num2]
else:
    sorted_order = [num3,num2,num1]

print("sorted order is",sorted_order)
