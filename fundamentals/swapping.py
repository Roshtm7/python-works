num1=100
num2=200

# write a program to swap 2 numbers
# values before swapping is num1=100 num2=200
# values after swapping is num1=200 num2=100 


#num1=num2 #num1=200
# num2=num1 #num2=100


#1)logic using temp variable - support in any lang
# temp = num1
# num1=num2
# num2 =temp 
# print(num1)
# print(num2)


#2)logic using addition and substraction - support in any lang
# num1=num1+num2 #num1=100+200=300
# num2=num1-num2 #num2=300-200=100
# num1=num1-num2 #num1=300-100=200



#3) logic - only support in python
# (num1,num2)=(num2,num1) or without braket also supports

#4) logic 4  using multiplication and division
# num1 = num1 * num2
# num2 = num1 / num2
# num1 = num1 / num2
# print(num1)
# print(num2)

# logic 5 using xor  
# XOR the two integers 'a' and 'b' and store its result in the integer 'a' itself.
# Now XOR the updated value of 'a' with 'b'. 
# This will result in the original value of 'a', which is now stored in 'b'.
num1= num1 ^ num2
num2  = num1 ^ num2
num1 = num1 ^ num2
print(num1)
print(num2)




