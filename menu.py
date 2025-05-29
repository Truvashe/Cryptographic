#Here the menu for the user

def menu0(user):
    print(f"Welcome {user} to your Text Encryptor, please choose one of the following options to continue (press a number) : ")
    print("\t1.Encrypt a message into an image")
    print("\t2.Decrypt a message from an image")
    print("\t3.List All users")
    print("\t4.Settings")
    print("\n\t0.Exit")
    a=int(input("Slect an option: "))

    if a >= 0 and a <=4:
        print(f"You have choosed option{a}")
        return a
    else:
        return -1

def menu_s(user):
    print("===============\nSETTINGS\n===============\n")
    print("\t1.Change User")
    print("\t2.Change Main Repesetory")
    print("\t3.Become Admin")
    print("\t4.Create User db file")
    print("\t5.Check files")
    print("\n\t0.Back")
    a=int(input("Slect an option: "))

    if a >= 0 and a <=5:
        print(f"You have choosed option{a}")
        return a
    else:
        return -1