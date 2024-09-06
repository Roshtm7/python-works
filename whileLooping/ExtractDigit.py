#extract number from user and print number

num = int(input("enter number"))
sum = 0
while(num!=0):
    digit=num%10
    print(digit)
    num=num//10
