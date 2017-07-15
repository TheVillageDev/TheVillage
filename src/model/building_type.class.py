class BuildingType ():
    """
    id # int NOT NULL,
    id_zeitalter # int
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         id_zeitalter: int
        """
        missing = "BuildingType __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "id_zeitalter" in kwargs.keys():
            self.id_zeitalter = int(kwargs["id_zeitalter"])

    def getId(self):
        return self.id

    def getIdZeitalter(self):
        return self.id_zeitalter

    def setIdZeitalter(self, id_zeitalter):
        self.id_zeitalter = id_zeitalter
