# 
from abc import ABCMeta


class Role(metaclass=ABCMeta):
    # protected:
    """
    id # int
    id_permission # int
    id_hierarchy_lvl_availability_bis # int
    """
    # public:
    def getId(self): 
        """
         @id:int
        """
        return self.id

    def getIdPermission(self):
        return self.id_permission

    def setIdPermission(self, id_permission):
        self.id_permission = int(id_permission)

    def getIdHierarchyLvlAvailability_bis(self):
        return self.id_hierarchy_lvl_availability_bis

    def setIdHierarchyLvlAvailability_bis(
            self, id_hierarchy_lvl_availability_bis):
        self.id_hierarchy_lvl_availability_bis =\
                int(id_hierarchy_lvl_availability_bis)

