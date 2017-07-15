class ClanRole ():
    """
    id # int NOT NULL,
    id_clan_authority_lvl_availability_von # int NOT NULL,
    id_clan_authority_lvl_availability_bis # int,
    id_clan_permission # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         id_clan_authority_lvl_availability_von: int NOT NULL,
         id_clan_authority_lvl_availability_bis: int,
         id_clan_permission: int NOT NULL
        """
        missing = "ClanRole __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "id_clan_authority_lvl_availability_von" in kwargs.keys():
            self.id_clan_authority_lvl_availability_von =\
                    int(kwargs["id_clan_authority_lvl_availability_von"])
        else:
            raise ValueError(missing+"id_clan_authority_lvl_availability_von")
        if "id_clan_authority_lvl_availability_bis" in kwargs.keys():
            self.id_clan_authority_lvl_availability_bis =\
                    int(kwargs["id_clan_authority_lvl_availability_bis"])
        if "id_clan_permission" in kwargs.keys():
            self.id_clan_permission = int(kwargs["id_clan_permission"])
        else:
            raise ValueError(missing+"id_clan_permission")

    def getId(self):
        return self.id

    def getIdClanAuthorityLvlAvailabilityVon(self):
        return self.id_clan_authority_lvl_availability_von

    def setIdClanAuthorityLvlAvailabilityVon(
            self, id_clan_authority_lvl_availability_von):
        self.id_clan_authority_lvl_availability_von =\
                int(id_clan_authority_lvl_availability_von)

    def getIdClanAuthorityLvlAvailabilityBis(self):
        return self.id_clan_authority_lvl_availability_bis

    def setIdClanAuthorityLvlAvailabilityBis(
            self, id_clan_authority_lvl_availability_bis):
        self.id_clan_authority_lvl_availability_bis =\
                int(id_clan_authority_lvl_availability_bis)

    def getIdClanPermission(self):
        return self.id_clan_permission

    def setIdClanPermission(self, id_clan_permission):
        self.id_clan_permission = int(id_clan_permission)
