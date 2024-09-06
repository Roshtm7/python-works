#write a program to find different conditions in signal

signal_light=input("enter light")
if(signal_light=="red"):
    print("stop")
elif(signal_light=="orange"):
    print("wait")
elif(signal_light=="green"):
    print("go")
else:
    print("no matching color")