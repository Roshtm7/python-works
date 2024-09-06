#read start limit and end limit from the user and print all odd numbers from the start limit and end limit
start = int(input("enter start number"))
end = int(input("enter end number"))
while(start<end):
    if(start%2!=0):
        print(start)
    start=start+1