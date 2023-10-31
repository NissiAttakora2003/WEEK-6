low = False
num = False
upp = False
lenght = False
special = False


def isdifgit(pas):
    num = False
    for i in pas:
        if i.isdigit():
            num = True
            break
    else:
        print("the password does not contain any digit")
    return num


def isUpper(pas):
    upp = False
    for i in pas:
        if i.isupper():
            upp = True
            break
    else:
        print("the password does not contain any upper letter")
    return upp


def islower(pas):
    low = False
    for i in pas:
        if i.lower():
            low = True
            break
    else:
        print("the password do not contain any lower case")
    return low


def lenghth(pas):
    lenght = False
    if (len(pas) > 8 and len(pas) < 13):
        lenght = True
    else:
        print("password does not meet the length requirement")
    return lenght


def special(pas):
    special = False
    for i in pas:
        if not i.isalnum():
            special = True
            break
    else:
        print("the password does not contain any special charcture")
    return special


if __name__ == "__main__":
    print(" Be between 8 and 12 character long")
    print(" Contain at least one uppercase letter")
    print(" Contain at least one lowercase letter")
    print(" Contain at least one digit")
    print(" Contain at least one 'special character'")
    invalid_password=True
    while invalid_password:
        pas = str(input("insert pass: "))
        isUpper(pas)  # check if the pssword contain any upper letter
        islower(pas)  # check id the password contain any lower case
        lenghth(pas)  # check is the password is lenghty enough
        special(pas)  # check if the password contain any special characture
        isdifgit(pas)  # chehck if the password conatain any digit

        if (islower(pas) and isdifgit(pas) and isUpper(pas) and lenghth(pas) and special(pas)) == True:
            print("Nice strong password")
            invalid_password=True
            break


