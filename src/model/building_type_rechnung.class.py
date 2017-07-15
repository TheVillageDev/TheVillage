class BuildingTypeRechnung ():
    """
    id # int NOT NULL,
    id_rechnung # int NOT NULL,
    id_building_type # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         id_rechnung: int NOT NULL,
         id_building_type: int NOT NULL
        """
        missing = "BuildingTypeRechnung __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "id_rechnung" in kwargs.keys():
            self.id_rechnung = int(kwargs["id_rechnung"])
        else:
            raise ValueError(missing+"id_rechnung")
        if "id_building_type" in kwargs.keys():
            self.id_building_type = int(kwargs["id_building_type"])
        else:
            raise ValueError(missing+"id_building_type")

    def getId(self):
        return self.id

    def getIdRechnung(self):
        return self.id_rechnung

    def setIdRechnung(self, id_rechnung):
        self.id_rechnung = id_rechnung

    def getIdBuildingType(self):
        return self.id_building_type

    def setIdBuildingType(self, id_building_type):
        self.id_building_type = id_building_type
