#write a program to print sum off all odd numbers from 1 to 100
start = 1
end = 100
sum = 0
while(start<=end):
    if(start%2!=0):
        sum = sum+start
    start = start +1
print(sum)
