#read a year from user
# print century year if it ends with two zero
# else print not century year

#program
# year=int(input("enter a year:"))
# if(year%100==0):
#     print("year is century")
# else:
#     print("not century")




# read a number from user
# print fizz if num is /by 3 -divisible
# print buss if num is / by 5
# print fizzbuss if num is /by 15

num=int(input("enter a number:"))
if(num==num/3):
    print("fizz")
elif(num==num/5):
    print("buzz")
elif(num==num/15):
    print("fizzbuzz")
else:
    print("invalid")


