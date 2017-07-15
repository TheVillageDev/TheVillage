class Zeitalter ():
    """
    id # int NOT NULL,
    min_fortschritts_lvl # float
    """
    def __init__(self, **kwargs):
        """
        @**kwargs:
         id: int NOT NULL,
         min_fortschritts_lvl: float
        """
        missing = "Zeitalter __init__: missing parameter "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "min_fortschritts_lvl" in kwargs.keys():
            self.min_fortschritts_lvl = float(kwargs["min_fortschritts_lvl"])

    def getId(self):
        return self.id

    def getMinFortschrittsLvl(self):
        return self.min_fortschritts_lvl

    def setMinFortschrittsLvl(self, min_fortschritts_lvl):
        self.min_fortschritts_lvl = min_fortschritts_lvl
