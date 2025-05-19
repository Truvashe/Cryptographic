import os

def chg_to_curr_rep():
    os.chdir("D:/ProjetPython")
    os.getcwd

def check_dir():
    if str(os.getcwd()) != "D:/ProjetPython":
        return False