class Friendlist ():
    """
    id # int NOT NULL,
    name # string NOT NULL,
    description # string,
    id_user # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         name: string NOT NULL,
         description: string,
         id_user: int NOT NULL
        """
        missing = "Friendlist __init__: missing parameter "
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
        if "id_user" in kwargs.keys():
            self.id_user = int(kwargs["id_user"])
        else:
            raise ValueError(missing+"id_user")

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getIdUser(self):
        return self.id_user

    def setIdUser(self, id_user):
        self.id_user = id_user
