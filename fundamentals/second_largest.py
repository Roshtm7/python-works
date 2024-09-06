#read 3 numbers from the users num1,num2,num3
#print the second largest number from the 3 number

num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))
if(num1>=num2 and num1<=num3 or num1>=num3 and num1<=num2):
    print(num1,"is the second largest")
elif(num2>=num1 and num2<=num3 or num2>=num3 and num2<=num1):
    print(num2,"is the second largest")
else:
    print(num3,"is the second largest")



#or


# if num1>num2 and num1>num3:
#     print(f"the largest number is{num1}")
#     if num2>num3:
#         print(f"the largest is{num2}")
#     else:
#         print(f"the largest is{num3}")
# elif num2>num3 and num2>num1:
#     print(f"the largest number is{num2}")
#     if num3>num1:
#         print(f"the largest is{num3}")
#     else:
#         print(f"the largest is{num1}")
# elif num3>num1 and num3>num2:
#     print(f"the largest number is{num3}")
#     if num1>num2:
#         print(f"the second largest is num1")
#     else:
#         print(f"the second largest is{num2}")
# elif num1==num2==num3:
#     print(f"three numbers are equal")


#or

# if num2>num1>num3 or num3>num1>num2:
#     print(f"the second largest number is {num1}")
# elif num1>num2>num3 or num3>num2>num1:
#     print(f"the second largest number is {num2}")
# else:
#     print(f"the second largest number is {num3}")

