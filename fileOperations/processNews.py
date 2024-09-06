f = open("/Users/admin/Desktop/PythonJune/fileOperations/news.txt","r")
word_list = []

for line in f:
    word = line.rstrip("\n")
    words = word.split(" ")

    for w in words:
        word_list.append(w)

# word_list = [w for line in f for w in line.rstrip("\n").split(" ") ] above program in a single line
wc = {w:word_list.count(w)for w in word_list if w !=""}
print(wc)

srt = sorted(wc,key=lambda key:wc.get(key),reverse = True)
print(srt)


    