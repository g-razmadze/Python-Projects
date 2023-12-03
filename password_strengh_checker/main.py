def pass_checker(password):
    Upperchars, lowerchars, digits, speacialChars = 0,0,0,0
    lenght = len(password)

    if lenght < 8 :
        print("Password must have at least 8 charachters")
    else:
        for i in range(0, lenght):
            if password[i].isupper():
                Upperchars += 1
            elif password[i].islower():
                lowerchars += 1
            elif password[i].isdigit():
                digits += 1
            else:
                speacialChars += 1
    if lowerchars != 0 and Upperchars != 0 and digits != 0 and speacialChars != 0:
        if lenght < 10:
            print("Your password is strong!")
        else:
            print("Your Password is medium level")
    else:
        if lowerchars == 0:
            print("Password must contain at least one lowercase character!")
        elif Upperchars == 0:
            print("Password must contain at least one uppercase character!")
        elif digits == 0:
            print("Password must contain at least one digit!")
        else:
            print("Password must contain at least one speacial character!")
        
password = input("Please write your password: ")


pass_checker(password)