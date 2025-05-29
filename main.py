import img_ctrl
import rep_ctrl

import user_int
import menu

import directory_and_file_management as DAFM

from classes import c_user

#functions
def option1(user):
    user_name=user.get_name()
    img=input("Entrez le nom de l'image: ")
    if (DAFM.check_image(img)):
        text=input("Etrez le text a crypté: ")
        img_ctrl.open_image_crypt(img,text,user_name)
        return True
    else:
        print("Image not found, please upload in the image before using the program.")
        return False
    
def option2(user):
    user_name=user.get_name()
    img=input("Entrez l'image à decrypté: ")
    if (DAFM.check_image(img)):
        img_ctrl.open_image_decrypt(img,user_name)
        return True
    else:
        print("Image not found, please upload in the image before using the program.")
        return False
    
def option3():
    DAFM.list_users()
    return True

def option4(user):
    #here menu for settings
    menu.menu_s(user)
    return True

def option5():
    global stillin
    stillin=False

#GOLBAL VARIABLES
user=c_user()

#script begin

#variable to end the programe when it goes false
stillin=True

#main script

DAFM.check_main_dir()

#auth user
info=user_int.ask_user_auth()
user.set_name(info[0])
user.set_is_admin("True")
info=("","","")

print("Main function START")
#main

while stillin==True:
    option=menu.menu0(user.name)

    while option == -1:
        print("Invalid Option")
        option=int(input("Select an option: "))
        if option <= 0 and option >= 5:
            break
        else:
            option =-1

    if option==1:
        option1(user)
    elif option==2:
        option2(user)
    elif option==3:
        option3()
    elif option==4:
        option4(user)
        #à faire
    elif option==5:
        print("The program will now terminate.")
        option5()

exit()