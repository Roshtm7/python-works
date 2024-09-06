#write a program using for loop to print odd numbers from one to hundred
start = 1
end = 101
sum = 0
for odd in range(start,end):
    if(odd%2!=0):
        sum = sum+odd
print(sum)