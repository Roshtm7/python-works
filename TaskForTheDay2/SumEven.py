#write a program using for loop to print sum of all even numbers from 1 to 100
start = 1
end = 101
sum = 0
for even in range(start,end):
    if(even%2==0):
        sum = sum+even
print(sum)
