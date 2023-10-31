
def isdifgit(pas):
    digit = False
    for i in pas:
        if i.isdigit():
            digit = True
            break
        else:
            print("the password does not contain any digit")
    return digit
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
    low=False
    for i in pas:
        if i.lower():
            low=True
            break
        else:
            print("the password do not contain any lower case")
    return low
def lenghth(pas):
    len=False
    for i in pas:
        if (len(pas) > 8 and len(pas) < 13):
            len=True
            break
        else:
            print("[assword does not meet the length requirement")
    return len

def special(pas):
    special=False
    for i in pas:
        if not i.isalnum():
            special=True
            break
        else:
            print("the passwoerd doesnopt contain any special charactutrer")
    return special
if __name__=="__main__":
    print(" Be between 8 and 12 character long")
    print(" Contain at least one uppercase letter")
    print(" Contain at least one lowercase letter")
    print(" Contain at least one digit")
    print(" Contain at least one 'special character'")
    pas =str(input("insert pass"))
    isdifgit(pas)# chehck if the password conatain any digit
    isUpper(pas)# check if the pssword contain any upper letter
    islower(pas)# check id the password contain any lower case
    lenghth(pas)# check is the password is lenghty enough
    special(pas)

