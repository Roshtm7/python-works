#read 2 numbers from user num1,num2
#print largest of the two numbers
#if both are equal print both are equal

num1 = int(input("enter your 1st number"))
num2 = int(input("enter your 2nd number"))
if(num1>num2):
    print(num1,"is the largest")
elif(num1 == num2):
    print("both are equal")
else:
    print(num2,"is the largest")
