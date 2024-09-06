#write a program using for loop to print all the even numbers from one to hundred

start = 1
end = 101
for even in range(start,end):
    if(even%2==0):
        print(even)
