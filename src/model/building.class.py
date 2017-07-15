class Building ():
    """
    id # int NOT NULL,
    arbeiter # int,
    ende_arbeit # time,
    level # float,
    id_user # int NOT NULL,
    id_building_type # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         arbeiter: int,
         ende_arbeit: time,
         level: float,
         id_user: int NOT NULL,
         id_building_type: int NOT NULL
        """
        missing = "Building __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "arbeiter" in kwargs.keys():
            self.arbeiter = int(kwargs["arbeiter"])
        if "ende_arbeit" in kwargs.keys():
            self.ende_arbeit = kwargs["ende_arbeit"]  # TODO type constroll
        if "level" in kwargs.keys():
            self.level = float(kwargs["level"])
        if "id_user" in kwargs.keys():
            self.id_user = int(kwargs["id_user"])
        else:
            raise ValueError(missing+"id_user")
        if "id_building_type" in kwargs.keys():
            self.id_building_type = int(kwargs["id_building_type"])
        else:
            raise ValueError(missing+"id_building_type")

    def getId(self):
        return self.id

    def getArbeiter(self):
        return self.arbeiter

    def setArbeiter(self, arbeiter):
        self.arbeiter = int(arbeiter)

    def getEndeArbeit(self):
        return self.ende_arbeit

    def setEndeArbeit(self, ende_arbeit):
        self.ende_arbeit = ende_arbeit  # TODO check type

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = float(level)

    def getIdUser(self):
        return self.id_user

    def setIdUser(self, id_user):
        self.id_user = int(id_user)

    def getIdBuildingType(self):
        return self.id_building_type

    def setIdBuildingType(self, id_building_type):
        self.id_building_type = int(id_building_type)
