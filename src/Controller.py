from abc import ABCMeta, abstractmethod


# class Controller ():
class Controller(metaclass=ABCMeta):
    # public:
    @abstractmethod
    def __init__(self, database):
        self.database = database
        self.itemList = []  # Array
        self.indexIdx = 0  # int
        # self.initiateAllFromDB()

    @abstractmethod
    def createItem(self, **kwargs):
        """
         @**kwargs: all parameter used to create an item
        """
        raise NotImplementedError

    @abstractmethod
    def delItem(self, id_item): 
        """
         @id_item:int
        """
        raise NotImplementedError

    @abstractmethod
    def initiateFromDB(self, id_item,  validation): 
        """
         @id_item:int
        """
        raise NotImplementedError

    @abstractmethod
    def initiateAllFromDB(self, validation): 
        """
        """
        raise NotImplementedError

    def setDatabase(self, database):
        self.database = database
        return True

    def addItem(self, item): 
        """
         @item:
        """
        duplicate = self.isItem(item.getId())
        if not duplicate:
            self.itemList.append(item)
            self.indexIdx += 1
            return True
        else:
            msg = "Item is a duplicate! (%s: id = %s)"
            print(msg % (type(item).__name__, item.getId()))
            return False

    def removeItem(self, id_item): 
        """
         @id_item:int
        """
        for i in self.itemList:
            if i.getId() == id_item:
                item = i
        if item:
            self.itemList.remove(item)
            self.indexIdx -= 1
            return True
        else:
            return False

    # private:
    def getItemById(self, id): 
        """
         @id:int
         @item
        """
        validation = False
        """
         isUpToDate gibt True zurück,
         wenn id ist nicht in usr
         gibt False zurück,
         wenn id ist in usr
        """
        upToDate = self.process.isUpToDate(self.table_name, id)
        removed = not self.process.isUpToDate(self.table_name, -id)
        if not upToDate:
            self.initiateFromDB(id)
            self.process.setUpToDate(self.table_name, id)
        elif removed:
            self.removeItem(id)
            self.process.setUpToDate(self.table_name, -id)
            return False
        for item in self.itemList:
            if item.getId() == id:
                validation = item
        if not validation:
            if self.initiateFromDB(id):
                for item in self.itemList:
                    if item.getId() == id:
                        validation = item
        return validation

    def isItem(self, id):
        validation = False
        for item in self.itemList:
            if item.getId() == id:
                validation = True
        return validation

    def getAllItems(self):
        """
         @itemList:Array
        """
        updates = self.process.getUpdates(self.table_name)
        for update in updates:
            if int(update) < 0:
                self.getItemById(-update)
            else:
                self.getItemById(update)
        return self.itemList

    # public:
    def getId(self, idx_permission):
        """
         @idx_permission:int
         @id:int
        """
        if self.indexIdx > idx_permission and idx_permission >= 0:
            id = self.itemList[idx_permission].getId()
            return id
        else:
            return False

    def getTableName(self):
        """
         @table_name:str
        """
        return self.table_name
