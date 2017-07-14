# 
from abc import ABCMeta


class Role(metaclass=ABCMeta):
    # protected:
    """
    id # int
    id_permission # int
    id_max_hierarchy_lvl # int
    """
    # public:
    def getId(self): 
        """
         @id:int
        """
        return self.id

    def getPermission(self): 
        """
         @id_permission:int
        """
        return self.id_permission

    def getMaxHierarchyLvl(self): 
        """
         @id_max_hierarchy_lvl:int
        """
        try:
            return self.id_max_hierarchy_lvl
        except:
            return False

