vehicle_numbers = [
    "KL09AR752",
    "KL07PR364",
    "KL06AX564",
    "KL05CR576",

]

f=open("/Users/admin/Desktop/PythonJune/fileOperations/vehicleNum.txt","w")
for num in vehicle_numbers:
    f.write(num+"\n")
    