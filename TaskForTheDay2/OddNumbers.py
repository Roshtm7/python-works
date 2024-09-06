#write a program using for loop to print all odd numbers from one to 100
start = 1
end = 101
for odd in range(start,end):
    if(odd%2!=0):
        print(odd)