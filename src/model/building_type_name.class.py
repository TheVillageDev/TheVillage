class BuildingTypeName ():
    """
    id # int NOT NULL,
    name # string NOT NULL,
    description # string,
    max_arbeiter # int,
    id_building_type # int NOT NULL,
    id_zeitalter # int
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         name: string NOT NULL,
         description: string,
         max_arbeiter: int,
         id_building_type: int NOT NULL,
         id_zeitalter: int
        """
        missing = "BuildingTypeName __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "name" in kwargs.keys():
            self.name = str(kwargs["name"])
        else:
            raise ValueError(missing+"name")
        if "description" in kwargs.keys():
            self.description = str(kwargs["description"])
        if "max_arbeiter" in kwargs.keys():
            self.max_arbeiter = int(kwargs["max_arbeiter"])
        if "id_building_type" in kwargs.keys():
            self.id_building_type = int(kwargs["id_building_type"])
        else:
            raise ValueError(missing+"id_building_type")
        if "id_zeitalter" in kwargs.keys():
            self.id_zeitalter = int(kwargs["id_zeitalter"])

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = str(name)

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = str(description)

    def getMaxArbeiter(self):
        return self.max_arbeiter

    def setMaxArbeiter(self, max_arbeiter):
        self.max_arbeiter = int(max_arbeiter)

    def getIdBuildingType(self):
        return self.id_building_type

    def setIdBuildingType(self, id_building_type):
        self.id_building_type = int(id_building_type)

    def getIdZeitalter(self):
        return self.id_zeitalter

    def setIdZeitalter(self, id_zeitalter):
        self.id_zeitalter = int(id_zeitalter)
