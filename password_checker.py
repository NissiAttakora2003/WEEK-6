
def validpass(pas):
    digit = False
    upp = False
    low = False
    special = False
    lenght = False
    invldpss=True
    while invldpss:
        for i in pas:
            if (len(pas) > 8 and len(pas) < 13):
                lenght = True
            if i.isdigit():
                digit = True
            if i.isupper():
                upp = True
            if i.lower():
                low = True
            if not i.isalnum():
                special = True
        if (digit and upp and low and special and lenght == True):
            print("Nice the password is strong")
            invldpss = False
        else:
            invldpss=True
            pas = str(input("insert password: "))
    return 0

if __name__ == '__main__':
        print(" Be between 8 and 12 character long")
        print(" Contain at least one uppercase letter")
        print(" Contain at least one lowercase letter")
        print(" Contain at least one digit")
        print(" Contain at least one 'special character'")
        pas = str(input("insert password: "))
        validpass(pas)






