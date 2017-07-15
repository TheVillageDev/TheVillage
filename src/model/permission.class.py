# 
class Permission ():
    # private:
    """
    id = 0 # int
    description = "" # string
    """

    def __init__(self, **kwargs):
        """
         @**kwargs:
          id: int
          description: string
        """
        missing = "Permission __init__: Missing "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "description" in kwargs.keys():
            self.description = str(kwargs["description"])

    # public:
    def getId(self): 
        """
         @id:int
        """
        return self.id

    def getDescription(self): 
        """
         @description:string
        """
        return self.description

    def setDescription(self, description):
        self.description = description

