class ResourceStack ():
    """
    id # int NOT NULL,
    amount_resource # int NOT NULL,
    id_resource # int NOT NULL,
    id_user # int,
    id_rechnung # int
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         amount_resource: int NOT NULL,
         id_resource: int NOT NULL,
         id_user: int,
         id_rechnung: int
        """
        missing = "ResourceStack __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "amount_resource" in kwargs.keys():
            self.amount_resource = int(kwargs["amount_resource"])
        else:
            raise ValueError(missing+"amount_resource")
        if "id_resource" in kwargs.keys():
            self.id_resource = int(kwargs["id_resource"])
        else:
            raise ValueError(missing+"id_resource")
        if "id_user" in kwargs.keys():
            self.id_user = int(kwargs["id_user"])
        if "id_rechnung" in kwargs.keys():
            self.id_rechnung = int(kwargs["id_rechnung"])

    def getId(self):
        return self.id

    def getAmountResource(self):
        return self.amount_resource

    def setAmountResource(self, amount_resource):
        self.amount_resource = int(amount_resource)

    def getIdResource(self):
        return self.id_resource

    def setIdResource(self, id_resource):
        self.id_resource = int(id_resource)

    def getIdUser(self):
        return self.id_user

    def setIdUser(self, id_user):
        self.id_user = int(id_user)

    def getIdRechnung(self):
        return self.id_rechnung

    def setIdRechnung(self, id_rechnung):
        self.id_rechnung = int(id_rechnung)
