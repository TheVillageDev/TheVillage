class ResourceProduction ():
    """
    id # int NOT NULL,
    id_resource # int NOT NULL,
    id_building_type # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         id_resource: int NOT NULL,
         id_building_type: int NOT NULL
        """
        missing = "ResourceProduction __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "id_resource" in kwargs.keys():
            self.id_resource = int(kwargs["id_resource"])
        else:
            raise ValueError(missing+"id_resource")
        if "id_building_type" in kwargs.keys():
            self.id_building_type = int(kwargs["id_building_type"])
        else:
            raise ValueError(missing+"id_building_type")

    def getId(self):
        return self.id

    def getIdResource(self):
        return self.id_resource

    def setIdResource(self, id_resource):
        self.id_resource = id_resource

    def getIdBuildingType(self):
        return self.id_building_type

    def setIdBuildingType(self, id_building_type):
        self.id_building_type = id_building_type
