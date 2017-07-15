class FriendlistUser ():
    """
    id # int NOT NULL,
    id_user # int NOT NULL,
    id_friendlist # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         id_user: int NOT NULL,
         id_friendlist: int NOT NULL
        """
        missing = "FriendlistUser __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "id_user" in kwargs.keys():
            self.id_user = int(kwargs["id_user"])
        else:
            raise ValueError(missing+"id_user")
        if "id_friendlist" in kwargs.keys():
            self.id_friendlist = int(kwargs["id_friendlist"])
        else:
            raise ValueError(missing+"id_friendlist")

    def getId(self):
        return self.id

    def getIdUser(self):
        return self.id_user

    def setIdUser(self, id_user):
        self.id_user = id_user

    def getIdFriendlist(self):
        return self.id_friendlist

    def setIdFriendlist(self, id_friendlist):
        self.id_friendlist = id_friendlist
