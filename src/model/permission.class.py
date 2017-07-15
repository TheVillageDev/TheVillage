# 
class Permission ():
    # private:
    """
    id # int
    name # string
    description # string
    """

    def __init__(self, **kwargs):
        """
         @**kwargs:
          id: int
          name: int
          description: string
        """
        missing = "Permission __init__: Missing "
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

    # public:
    def getId(self): 
        """
         @id:int
        """
        return self.id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = str(name)

    def getDescription(self): 
        """
         @description:string
        """
        return self.description

    def setDescription(self, description):
        self.description = str(description)

