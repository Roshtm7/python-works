lst = [1,2,3,4,5,6,7]
squares = [n**2 for n in lst]
cube = [n**3 for n in lst]
odd_numbers = [n for n in lst if n%2!=0]
even_numbers = [n for n in lst if n%2==0]
print(squares)
print(cube)
print(odd_numbers)
print(even_numbers)

