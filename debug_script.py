import user_int

import directory_and_file_management as DAFM

import os

import img_ctrl

from classes import c_user 

user=c_user()

info=user_int.ask_user_auth()
user.set_name(info[0])
user.set_is_admin("True")
print(info)

print(user.name)
print(user.is_admin)

user_name=user.get_name()

print(user.get_name())