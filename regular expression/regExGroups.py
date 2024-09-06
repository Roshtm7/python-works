from re import finditer
text = "abc123 @k#7lMdef"
pattern = "[a-zA-z0-9]" 
matcher = finditer(pattern,text)
for m in matcher:
    print(m.start(),"===",m.group())

    