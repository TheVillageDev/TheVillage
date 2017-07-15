class ClanMembership ():
    """
    id # int NOT NULL,
    id_clan_authority_lvl # int NOT NULL,
    id_clan # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         id_clan_authority_lvl: int NOT NULL,
         id_clan: int NOT NULL
        """
        missing = "ClanMembership __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "id_clan_authority_lvl" in kwargs.keys():
            self.id_clan_authority_lvl = int(kwargs["id_clan_authority_lvl"])
        else:
            raise ValueError(missing+"id_clan_authority_lvl")
        if "id_clan" in kwargs.keys():
            self.id_clan = int(kwargs["id_clan"])
        else:
            raise ValueError(missing+"id_clan")

    def getId(self):
        return self.id

    def getIdClanAuthorityLvl(self):
        return self.id_clan_authority_lvl

    def setIdClanAuthorityLvl(self, id_clan_authority_lvl):
        self.id_clan_authority_lvl = int(id_clan_authority_lvl)

    def getIdClan(self):
        return self.id_clan

    def setIdClan(self, id_clan):
        self.id_clan = int(id_clan)
