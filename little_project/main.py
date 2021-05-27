def split(list, delim):
    temp = ""
    for i in list:
        temp += i
        temp += delim

    return temp


words = ["hello", "world", "this", "will", "be", "a", "string"]
delims = ["-", ":", " ", "+"]

for d in delims:
    print(split(words, d))


NUMBER = 0
NUMBER = 10

print(NUMBER)
