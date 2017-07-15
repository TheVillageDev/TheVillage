# 
from .Role import Role


class HierarchyRole (Role):
    # private:
    """
    id_hierarchy_lvl_availability_von # int
    """

    def __init__(self, **kwargs):
        """
         @**kwargs:
          id: int
          id_permission: int
          id_hierarchy_lvl_availability_von: int
          id_hierarchy_lvl_availability_bis: int = None
        """
        missing = "HierarchyRole __init__: Missing "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "id_permission" in kwargs.keys():
            self.id_permission = int(kwargs["id_permission"])
        else:
            raise ValueError(missing+"id_permission")
        if "id_hierarchy_lvl_availability_von" in kwargs.keys():
            self.id_hierarchy_lvl =\
                    int(kwargs["id_hierarchy_lvl_availability_von"])
        else:
            raise ValueError(missing+"id_hierarchy_lvl_availability_von")
        if "id_hierarchy_lvl_availability_bis" in kwargs.keys():
            self.id_max_hierarchy_lvl =\
                    int(kwargs["id_hierarchy_lvl_availability_bis"])

    def getIdHierarchyLvlAvailability_von(self):
        return self.id_hierarchy_lvl_availability_von

    def setIdHierarchyLvlAvailability_von(
            self, id_hierarchy_lvl_availability_von):
        self.id_hierarchy_lvl_availability_von =\
                id_hierarchy_lvl_availability_von

