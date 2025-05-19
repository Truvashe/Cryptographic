import img_ctrl
import rep_ctrl

import user_int
import menu

import directory_and_file_management as DAFM

#functions
def option1(user):
    img=input("Entrez le nom de l'image: ")
    if (DAFM.check_image(img)):
        text=input("Etrez le text a crypté: ")
        img_ctrl.open_image_crypt(img,text,user)
        return True
    else:
        print("Image not found, please upload in the image before using the program.")
        return False
    
def option2(user):
    img=input("Entrez l'image à decrypté: ")
    if (DAFM.check_image(img)):
        img_ctrl.open_image_decrypt(img,user,img_ctrl.get_wlist(user))
        return True
    else:
        print("Image not found, please upload in the image before using the program.")
        return False
    
def option3():
    DAFM.list_users()
    return True

def option4():
    #here menu for settings
    return True

def option5():
    stillin=False

#GOLBAL VARIABLES
user=""

#script begin

#variable to end the programe when it goes false
stillin=True

#main script

DAFM.check_main_dir()

#auth user
user=user_int.ask_user_auth()

#main

while stillin==True:
    option=menu.menu0

    while True:
        if option == -1:
            print("Invalid Option")
            option=input("Select an option: ")
            if option>0 and option<5:
                break

    if option==1:
        option1(user)
    elif option==2:
        option2(user)
    elif option==3:
        option3()
    elif option==4:
        option4()
        #à faire
    elif option==5:
        option5()