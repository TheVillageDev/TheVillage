class ZeitalterBuildingTypeRequirement ():
    """
    id # int NOT NULL,
    min_level # float,
    id_building_type # int NOT NULL,
    id_zeitalter # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         min_level: float,
         id_building_type: int NOT NULL,
         id_zeitalter: int NOT NULL
        """
        missing =\
            "ZeitalterBuildingTypeRequirement __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "min_level" in kwargs.keys():
            self.min_level = float(kwargs["min_level"])
        if "id_building_type" in kwargs.keys():
            self.id_building_type = int(kwargs["id_building_type"])
        else:
            raise ValueError(missing+"id_building_type")
        if "id_zeitalter" in kwargs.keys():
            self.id_zeitalter = int(kwargs["id_zeitalter"])
        else:
            raise ValueError(missing+"id_zeitalter")

    def getId(self):
        return self.id

    def getMinLevel(self):
        return self.min_level

    def setMinLevel(self, min_level):
        self.min_level = float(min_level)

    def getIdBuildingType(self):
        return self.id_building_type

    def setIdBuildingType(self, id_building_type):
        self.id_building_type = int(id_building_type)

    def getIdZeitalter(self):
        return self.id_zeitalter

    def setIdZeitalter(self, id_zeitalter):
        self.id_zeitalter = int(id_zeitalter)
