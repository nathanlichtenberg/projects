counter = 0
while counter < 10: 
    word = input("Your word: ")

    if word == word[::-1]:
        print("palindrome")
    else:
        print("ur a foot")

    counter += 1
