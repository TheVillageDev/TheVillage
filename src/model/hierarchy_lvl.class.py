# 
class HierarchyLvl ():
    """
    id # int
    name # string
    description # string
    ids_hierarchy_role # array
    """
    # public:

    def __init__(self, **kwargs):
        """
           @**kwargs:
          id: int
          name: string
          description: string
          ids_hierarchy_role: Array
        """
        missing = "HierarchyLvl __init__: Missing "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "name" in kwargs.keys():
            self.id = str(kwargs["name"])
        else:
            raise ValueError(missing+"name")
        if "description" in kwargs.keys():
            self.description = str(kwargs["description"])
        if "ids_hierarchy_role" in kwargs.keys():
            self.ids_hierarchy_role = list(kwargs["ids_hierarchy_role"])

    def getId(self):
        """
         @id:int
        """
        return self.id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    """
    hierarchy lvl stuff
    """
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

