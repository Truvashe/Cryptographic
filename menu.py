import img_ctrl

#Here the menu for the user

def menu0():
    print("Welcome to your Text Encryptor, please choose one of the following options to continue (press a number) : ")
    print("\t1.Encrypt a message into an image")
    print("\t2.Decrypt a message from an image")
    print("\t3.List All users")
    print("\t4.Settings")
    print("\t5.Exit")
    a=input("Slect an option: ")

    if a >= 1 and a <=5:
        return a
    else:
        return -1

