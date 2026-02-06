ch = input("Enter a character: ")

if len(ch) == 1:
    ASCII_value = ord(ch)
    print("The ASCII value is:", ASCII_value)
else:
    print("Please enter only one character.")