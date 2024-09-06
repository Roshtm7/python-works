f_read = open("/Users/admin/Desktop/PythonJune/fileOperations/years.txt","r")
f_century = open("/Users/admin/Desktop/PythonJune/fileOperations/century.txt","w")
f_non_century = open("/Users/admin/Desktop/PythonJune/fileOperations/non_century.txt","w")

for year in f_read:
    y = int(year.rstrip("\n"))
    if y%100==0:
        f_century.write(str(y)+"\n")
    else:
        f_non_century.write(str(y)+"\n")
        