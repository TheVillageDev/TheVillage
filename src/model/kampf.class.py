class Kampf ():
    """
    id # int NOT NULL,
    angreifer_truppen # int NOT NULL,
    verteidiger_truppen # int,
    gewonnen # bool,
    timestamp # time NOT NULL,
    id_user_angreifer # int NOT NULL,
    id_user_verteidiger # int NOT NULL
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         angreifer_truppen: int NOT NULL,
         verteidiger_truppen: int,
         gewonnen: bool,
         timestamp: time NOT NULL,
         id_user_angreifer: int NOT NULL,
         id_user_verteidiger: int NOT NULL
        """
        missing = "Kampf __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "angreifer_truppen" in kwargs.keys():
            self.angreifer_truppen = int(kwargs["angreifer_truppen"])
        else:
            raise ValueError(missing+"angreifer_truppen")
        if "verteidiger_truppen" in kwargs.keys():
            self.verteidiger_truppen = int(kwargs["verteidiger_truppen"])
        if "gewonnen" in kwargs.keys():
            self.gewonnen = bool(kwargs["gewonnen"])
        if "timestamp" in kwargs.keys():
            self.timestamp = kwargs["timestamp"]  # TODO type constroll
        else:
            raise ValueError(missing+"timestamp")
        if "id_user_angreifer" in kwargs.keys():
            self.id_user_angreifer = int(kwargs["id_user_angreifer"])
        else:
            raise ValueError(missing+"id_user_angreifer")
        if "id_user_verteidiger" in kwargs.keys():
            self.id_user_verteidiger = int(kwargs["id_user_verteidiger"])
        else:
            raise ValueError(missing+"id_user_verteidiger")

    def getId(self):
        return self.id

    def getAngreiferTruppen(self):
        return self.angreifer_truppen

    def setAngreiferTruppen(self, angreifer_truppen):
        self.angreifer_truppen = int(angreifer_truppen)

    def getVerteidigerTruppen(self):
        return self.verteidiger_truppen

    def setVerteidigerTruppen(self, verteidiger_truppen):
        self.verteidiger_truppen = int(verteidiger_truppen)

    def getGewonnen(self):
        return self.gewonnen

    def setGewonnen(self, gewonnen):
        self.gewonnen = bool(gewonnen)

    def getTimestamp(self):
        return self.timestamp

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp  # TODO check type

    def getIdUserAngreifer(self):
        return self.id_user_angreifer

    def setIdUserAngreifer(self, id_user_angreifer):
        self.id_user_angreifer = int(id_user_angreifer)

    def getIdUserVerteidiger(self):
        return self.id_user_verteidiger

    def setIdUserVerteidiger(self, id_user_verteidiger):
        self.id_user_verteidiger = int(id_user_verteidiger)
