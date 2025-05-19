import os
import getpass
import directory_and_file_management as DAFM

def sign_in():
    print("Veuillez Entrez un nom de minimum 2 charactéres et max 10, puis un mot de passe")

    while True:
        a=("Entrez votre nom :")
        if len(a)<10 and len(a)<10:
            break
        if check_user_db_u(a):
            print("User name already in db")
        print("Error, please try again.")

    while True:
        b=getpass.getpass("Entrez votre mdp: ")
        c=getpass.getpass("Confirmez votre mdp: ")

        if a==b:
            break
        print("Error, please try again.")

    save=("Press Y to save, or N to exit the sign in process")

    if save=="Y":
        if check_user_db():
            save_user(a,b)
            return True
        else:
            DAFM.creat_usr_file
            save_user(a,b)
            return False
    else:
        return False

def save_user(name,pswrd):
    file=open("user_db.csv","a")
    file.write(f"{name},{pswrd}")

    print("You're User-Name and Password have been saved.")
    return True

def ask_user_auth():
    print("Veuillez saisir votre nom et mdp")
    a=input("Entrez votre nom: ")
    b=input("Entrez votre mdp: ")

    if check_user_db_up(a,b):
        return a,b
    else:
        return False

def check_user_db_up(user,pswrd):
    if os.path.isfile("user_db.csv"):
        file=open("user_db.csv","r")
        lines=file.readlines()

        file.close()

        for line in lines:
            line=line.split(",")
            if line[0]==user and line[1]==pswrd:
                return True
        return False
    
def check_user_db_u(user):
    if os.path.isfile("user_db.csv"):
        file=open("user_db.csv","r")
        lines=file.readlines()

        file.close()

        for line in lines:
            if line[0]==user:
                return True
        return False

def check_user_db():
    if os.path.isfile("user_db.csv"):
        return True
    print("User File Data base is messing")
    return False  
        

def ask_txt_to_crypt():
    #I prefer to use this function with a tuple for no reason hh
    a=input("Entrez le text à crypté :")
    return (a,len(a))

#get all whitelisted names of a user in a list
def get_wlist(user_name):

    with open("white_list.csv", "r") as file:
        lines = file.readlines()

    dictionary = {}

    for line in lines:
        parts = line.strip().split(',')
        if len(parts) < 2:
            continue  # skip malformed lines
        name = parts[0]
        whitelist = parts[1:]
        dictionary[name] = whitelist

    return dictionary.get(user_name, [])