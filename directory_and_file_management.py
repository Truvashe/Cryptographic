import os

#GOLBAL VARIABLES
main_dir=""

def check_main_dir():
    print("This is the actual directory :")
    os.getcwd

    a=input("Do you want to change it ? (y/n) :")
    b=True #loop activator

    while b==True:
        if a=="y" or a=="yes":
            chg_main_dir()
            b=False
            return True
        elif a=="n" or a=="no":
            b=False
            return False
        else:
            print("Answer non-recognisable please try again")

def chg_main_dir():
    global main_dir

    #loop holder
    a="n"
    while (a=="n" or a=="no"):
        main_dir=input("Write your new directory : ")
        a=input(f"Your new directory has been set to : {str(main_dir)}\nDo you want to keep it ? (y/n)")
        if os.path.isdir(main_dir):
            a="y"
            print("Your directory has been changed succefully")
            return True
        else:
            print("The path you entered is INVALID please try again")
            a="n"
    return False

#create_user_file

def creat_usr_file(main_dir):

    if main_dir=="":
        print("Main directory empty, please insert a valid directory to put in users data base")
        if check_main_dir()==False:
            print("ERROR : You have no directory to put in the file")
            return False
    else:
        if os.path.isfile("user_db.csv"):
            print("The user data base file already exist in this directory\nHere are all the files of the current directory :")
            os.listdir()
            return False
    
    file=open("user_db.csv","w")
    return True

#list users
def list_users():
    if os.path.isfile("user_db.csv"):
        with open("user_db.csv", "r") as file:
            lines = file.readlines()

        for line in lines:
            parts = line.strip().split(",")
            if parts:
                print(parts[0])

#Check for image

def check_image(img):
    files=os.listdir

    if img in files:
        return True
    return False