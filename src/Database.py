# 
from abc import ABCMeta, abstractmethod

# class Database ( metaclass=ABCMeta ):
class Database ():
    #private:

    #public:
    @abstractmethod
    def __init__( self, database,  username,  password,  host = "localhost"): 
        """
         @database:string
         @username:string
         @password:string
         @host:string
        """
        self.database=database
        self.username=username
        self.password=password
        self.host=host

    @abstractmethod
    def insert( self, table_name,  **kwargs): 
        """
         @table_name:string
         @**kwargs:key=val,key2=val
        """
        raise NotImplementedError

    @abstractmethod
    def update( self, table_name, id, **kwargs ):
        """
         @table_name:string
         @id:int
         @**kwargs:key=val,key2=val
        """
        raise NotImplementedError
    
    @abstractmethod
    def delete( self, table_name, id ):
        """
         @table_name:string
         @id:int
        """
        raise NotImplementedError

    @abstractmethod
    def loadTable( self, table_name): 
        """
         @table_name:string
        """
        raise NotImplementedError

    @abstractmethod
    def load( self, table_name,  id): 
        """
         @table_name:string
         @id:int
        """
        raise NotImplementedError

    @abstractmethod
    def loadForeignKeys( self, table, table_id_name, join_table, join_table_id_value):
        """
         @table:string
         @table_id_name:string
         @join_table:string
         @join_table_id_value:string
         SELECT `table`.`id` FROM `table`
         JOIN `join_table`
         ON `join_table`.`id` LIKE `table`.`table_id_name`
         WHERE `join_table`.`id` LIKE "join_table_id_value"
        """
        raise NotImplementedError



