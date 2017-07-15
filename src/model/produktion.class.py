class Produktion ():
    """
    id # int NOT NULL,
    id_item_type # int NOT NULL,
    id_building_type # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         id_item_type: int NOT NULL,
         id_building_type: int NOT NULL
        """
        missing = "Produktion __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "id_item_type" in kwargs.keys():
            self.id_item_type = int(kwargs["id_item_type"])
        else:
            raise ValueError(missing+"id_item_type")
        if "id_building_type" in kwargs.keys():
            self.id_building_type = int(kwargs["id_building_type"])
        else:
            raise ValueError(missing+"id_building_type")

    def getId(self):
        return self.id

    def getIdItemType(self):
        return self.id_item_type

    def setIdItemType(self, id_item_type):
        self.id_item_type = id_item_type

    def getIdBuildingType(self):
        return self.id_building_type

    def setIdBuildingType(self, id_building_type):
        self.id_building_type = id_building_type
