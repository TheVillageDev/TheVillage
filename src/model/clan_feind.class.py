class ClanFeind ():
    """
    id # int NOT NULL,
    id_clan_1 # int NOT NULL,
    id_clan_2 # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         id_clan_1: int NOT NULL,
         id_clan_2: int NOT NULL
        """
        missing = "ClanFeind __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "id_clan_1" in kwargs.keys():
            self.id_clan_1 = int(kwargs["id_clan_1"])
        else:
            raise ValueError(missing+"id_clan_1")
        if "id_clan_2" in kwargs.keys():
            self.id_clan_2 = int(kwargs["id_clan_2"])
        else:
            raise ValueError(missing+"id_clan_2")

    def getId(self):
        return self.id

    def getIdClan1(self):
        return self.id_clan_1

    def setIdClan1(self, id_clan_1):
        self.id_clan_1 = id_clan_1

    def getIdClan2(self):
        return self.id_clan_2

    def setIdClan2(self, id_clan_2):
        self.id_clan_2 = id_clan_2
