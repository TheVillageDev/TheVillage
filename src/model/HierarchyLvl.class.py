# 
class HierarchyLvl ():
    """
     @Author: Marco
    """
    # private:
    id = None  # int
    description = ""  # string
    ids_hierarchy_role = []  # array
    ids_user = []  # array
    # public:

    def __init__(self, **kwargs):
        """
           @**kwargs:
          id: int
          description: string
          ids_hierarchy_role: Array
        """
        missing = "HierarchyLvl __init__: Missing "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "description" in kwargs.keys():
            self.description = str(kwargs["description"])
        if "ids_hierarchy_role" in kwargs.keys():
            self.ids_hierarchy_role = list(kwargs["ids_hierarchy_role"])

    def getId(self):
        """
         @id:int
        """
        return self.id

    def getDescription(self): 
        """
         @description:string
        """
        return self.description

    def getHierarchyRoles(self): 
        """
         @ids_hierarchy_role:array
        """
        return self.ids_hierarchy_role

    def addHierarchyRole(self, id):
        if id in self.ids_hierarchy_role:
            return False
        else:
            self.ids_hierarchy_role.append(int(id))
            return True

    def removeHierarchyRole(self, id):
        if int(id) in self.ids_hierarchy_role:
            self.ids_hierarchy_role.remove(id)
            return True
        else:
            return False

