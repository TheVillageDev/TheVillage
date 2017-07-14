# 
from .Role import Role


class UserRole (Role):
    # private:
    """
    id_user = None # int
    """

    def __init__(self, **kwargs):
        """
         @**kwargs:
          id: int
          id_user: int
          id_permission: int
          id_max_hierarchy_lvl: int = None
        """
        missing = "UserRole __init__: Missing "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "id_user" in kwargs.keys():
            self.id_user = int(kwargs["id_user"])
        else:
            raise ValueError(missing+"id_user")
        if "id_permission" in kwargs.keys():
            self.id_permission = int(kwargs["id_permission"])
        else:
            raise ValueError(missing+"id_permission")
        if "id_max_hierarchy_lvl" in kwargs.keys():
            self.id_max_hierarchy_lvl = int(kwargs["id_max_hierarchy_lvl"])

    def getUser(self):
        """
         @id_user: int
        """
        return self.id_user
