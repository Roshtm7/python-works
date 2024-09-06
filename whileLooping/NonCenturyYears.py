#print all non century years from 1800 to 2024
start = 1800
end = 2024
while(start<=end):
    if(start%100!=0):
        print(start)
    start = start+1