text1 = input("Enter a line of text:")
words = text1.split(' ')
for i in set(words):
    print(i, " : ", words.count(i))
