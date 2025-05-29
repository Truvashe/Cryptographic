class c_user:
    def __init__(self,name="GUEST"):
        self.name = name
        self.is_admin = False

    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name=name

    def get_is_admin(self):
        return self.is_admin
    
    def set_is_admin(self,value):
        print("Setting ADMIN")
        if (isinstance(value, str)) and (value.lower() in ["true", "1", "yes", "on"]):
            print("Admin SET")
            self.is_admin = True
        else:
            self.is_admin = False
            print("Couldn't make Admin, Value ERROR.")

    
    def make_admin(self):
        self.is_admin=True

    def unmake_admin(self):
        self.is_admin=False
