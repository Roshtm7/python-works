#write a program using for loop to print cubes of all numbers from 1 to 50

start = 1
end = 51
cube = 1 
for i in range(start,end):
    cube = start**3
    start = start+1
print(cube)

