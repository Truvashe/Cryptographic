import os
import rep_ctrl

#GOLBAL VARIABLES
main_dir=""

#to delete when exporting
rep_ctrl.chg_to_curr_rep()
main_dir="D:/ProjetPython"

import os

def check_main_dir():
    print("This is the actual directory :")
    print(os.getcwd())

    while True:
        try:
            a = input("Do you want to change it? (y/n): ").strip().lower()
            if a in ("y", "yes"):
                chg_main_dir()
                return True
            elif a in ("n", "no"):
                return False
            else:
                raise ValueError("Answer not recognizable")
        except ValueError as e:
            print(e)

def chg_main_dir():
    global main_dir
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
    file.close()
    return True

def list_users():
    if os.path.isfile("user_db.csv"):
        with open("user_db.csv", "r") as file:
            lines = file.readlines()

        for line in lines:
            parts = line.strip().split(",")
            if parts:
                print(parts[0])


def check_image(img):
    files=str(os.listdir())

    if str(img) in files:
        return True
    return False