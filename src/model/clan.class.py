class Clan ():
    """
    id # int NOT NULL,
    name # string NOT NULL,
    description # string
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         name: string NOT NULL,
         description: string
        """
        missing = "Clan __init__: missing parameter "
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
