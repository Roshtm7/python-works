#read height and weight from the user and calculate bmi
#print underweight if bmi<19
#print normal weight if bmi ranges 19 to 25
#print overweight if bmi in range of 25 to 35
#print obesity

height = float(input("enter height"))/100
weight = float(input("enter weight"))
bmi = weight/height**2
if(bmi<=19):
    print("underweight")
elif(19<=bmi<=25):
    print("normalweight")
elif(25<=bmi<=30):
    print("overweight")
else:
    print("obesity")
