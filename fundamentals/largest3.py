#read 3 numbers from user num1,num2,num3
#print largest among the 3 numbers

num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))
if(num1>num2 and num1>num3):
    print(num1,"is the largest")
elif(num2>num3):
    print(num2,"is the largest")
else:
    print(num3,"is the largest")