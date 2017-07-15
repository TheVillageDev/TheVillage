class ItemStack ():
    """
    id # int NOT NULL,
    amount_item # int NOT NULL,
    id_user # int NOT NULL,
    id_item_type # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         amount_item: int NOT NULL,
         id_user: int NOT NULL,
         id_item_type: int NOT NULL
        """
        missing = "ItemStack __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "amount_item" in kwargs.keys():
            self.amount_item = int(kwargs["amount_item"])
        else:
            raise ValueError(missing+"amount_item")
        if "id_user" in kwargs.keys():
            self.id_user = int(kwargs["id_user"])
        else:
            raise ValueError(missing+"id_user")
        if "id_item_type" in kwargs.keys():
            self.id_item_type = int(kwargs["id_item_type"])
        else:
            raise ValueError(missing+"id_item_type")

    def getId(self):
        return self.id

    def getAmountItem(self):
        return self.amount_item

    def setAmountItem(self, amount_item):
        self.amount_item = amount_item

    def getIdUser(self):
        return self.id_user

    def setIdUser(self, id_user):
        self.id_user = id_user

    def getIdItemType(self):
        return self.id_item_type

    def setIdItemType(self, id_item_type):
        self.id_item_type = id_item_type
