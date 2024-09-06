# read a number from user
# print fizz if num is /by 3 -divisible
# print buss if num is / by 5
# print fizzbuss if num is /by 15

#  here we have to use modulus operator

num=int(input("enter a number:"))
if(num%3==0):
    print("fizz")
elif(num%5==0):
    print("buzz")
elif(num%15==0):
    print("fizzbuzz")
else:
    print("invalid")