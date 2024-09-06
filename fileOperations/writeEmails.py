emailid = [
    "mohammed@gmail.com",
    "wilson@gmail.com",
    "parvathi@email.com,",
    "rintu@email.com",
]

f = open("/Users/admin/Desktop/PythonJune/fileOperations/emailid.txt","w")
for email in emailid:
    f.write(email+"\n") 