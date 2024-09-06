#read start_limit and end_limit from the user by using for loop print odd numbers
start = int(input("enter number"))
end = int(input("enter number"))
for odd in range(start,end):
    if(odd%2!=0):
        print(odd)