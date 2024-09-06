#bitwise operator
#(&,|,^)
# lsb=least significant bit
# msb=most significant bit


#representation of numbers in bit
# 0=0000
# 1=0001
# 2=0010
# 3=0011
# 4=0100
# 5=0101
# 6=0110
# 7=0111
# 8=1000
# 9=1001



# print(1^0)
# 2
# 1

print(2&4) #0
# 0010
# 0100
# ====
# 0110

print(2|4)
# 0010
# 0100
# ====
# 0110

print(3&4)
#0011
#0100
#====
#0000 =>0
print(4|3)
#0100
#0011
#====
#0111 =7
print(2^4)
#0010
#0100
#====
#0110 = 6


# X    Y    X&Y    X|Y    X^Y
# 0    1    0       1      1
# 0    0    0       0      0
# 1    1    1       1      0
# 1    0    0       1      1



print(1&0)