def longest(string1):
    longest = 0
    for words in string1.split(","):
        if(len(words)>longest):
            longest = len(words)
            temp=words
    print("The list of words are:", string1)
    print("The longest word in the list is:", temp)
    print("The length of longest word in the list is:", longest)

string1 = input("Enter a list of words(separate it between commas):")
longest(string1);