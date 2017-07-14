# 
class User ():
    # private:
    """
    id # int
    username # string
    id_hierarchy_lvl # int
    ids_user_role # array
    """
    def __init__(self, **kwargs):
        """
         @**kwargs:
          id: int
          username: string  
          id_hierarchy_lvl: int
          ids_user_role: array = []
        """
        missing = "User __init__: Missing "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "username" in kwargs.keys():
            self.username = str(kwargs["username"])
        else:
            raise ValueError(missing+"username")
        if "id_hierarchy_lvl" in kwargs.keys():
            self.id_hierarchy_lvl = int(kwargs["id_hierarchy_lvl"])
        else:
            raise ValueError(missing+"id_hierarchy_lvl")
        if "ids_user_role" in kwargs.keys():
            self.ids_user_role = list(kwargs["ids_user_role"])
        else:
            self.ids_user_role = []

    # public:
    def getId(self):
        """
         @id:int
        """
        return self.id

    def getUsername(self): 
        """
         @username:string
        """
        return self.username

    def setUsername(self, new_username): 
        """
         @new_username:string
        """
        self.username = str(new_username)
        return True

    def getHierarchyLvl(self): 
        """
         @hierarchy_roles:
        """
        return self.id_hierarchy_lvl

    def upgrade(self): 
        """
        """
        self.id_hierarchy_lvl -= 1
        return True

    def downgrade(self): 
        """
        """
        self.id_hierarchy_lvl += 1
        return True

    def getUserRoles(self): 
        """
         @user_roles:array
        """
        return self.ids_user_role

    def addUserRole(self, id_user_role): 
        """
         @id_user:int
        """
        if int(id_user_role) in self.ids_user_role:
                return False
        else:
                self.ids_user_role.append(int(id_user_role))
                return True

    def removeUserRole(self, id_user_role): 
        """
         @id_user:int
        """
        if int(id_user_role) in self.ids_user_role:
                self.ids_user_role.remove(int(id_user_role))
                return True
        else:
                return False
