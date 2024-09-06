text = "the quick brown fox jumps over a lazy dog"
text = text.casefold()
ispanagram = True
alphabets = "abcdefghijklmnopqrstuvwxyz"
for ch in alphabets:
    if text.count(ch)==0:
        ispanagram = False
        break
print(ispanagram)