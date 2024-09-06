# word = "i have 1 bike and 2 car"
# for ch in word:
#     if ch.isalpha():
#         print(ch,end=",")

# for ch in word:
#     if ch.isdigit():
#         print(ch,end = ",")

word = "The quick brown fox jumps over the lazy dog"
word = word.casefold()
print(word)
alphabets = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
is_panagram = True
for ch in alphabets:
    if word.count(ch) == 0:
         is_panagram = False
         break
    print(is_panagram)
