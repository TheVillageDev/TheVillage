class Resource ():
    """
    id # int NOT NULL,
    name # string NOT NULL,
    id_zeitalter_availability_von # int,
    id_zeitalter_availability_bis # int
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         name: string NOT NULL,
         id_zeitalter_availability_von: int,
         id_zeitalter_availability_bis: int
        """
        missing = "Resource __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "name" in kwargs.keys():
            self.name = str(kwargs["name"])
        else:
            raise ValueError(missing+"name")
        if "id_zeitalter_availability_von" in kwargs.keys():
            self.id_zeitalter_availability_von =\
                    int(kwargs["id_zeitalter_availability_von"])
        if "id_zeitalter_availability_bis" in kwargs.keys():
            self.id_zeitalter_availability_bis =\
                    int(kwargs["id_zeitalter_availability_bis"])

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getIdZeitalterAvailabilityVon(self):
        return self.id_zeitalter_availability_von

    def setIdZeitalterAvailabilityVon(self, id_zeitalter_availability_von):
        self.id_zeitalter_availability_von = id_zeitalter_availability_von

    def getIdZeitalterAvailabilityBis(self):
        return self.id_zeitalter_availability_bis

    def setIdZeitalterAvailabilityBis(self, id_zeitalter_availability_bis):
        self.id_zeitalter_availability_bis = id_zeitalter_availability_bis
