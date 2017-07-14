# 
from .Database import Database
import pymysql


class MySqlDatabase (Database):
    """
     @self.database:string
     @self.username:string
     @self.password:string
     @self.host:string
     @self.db: MySql connection
     @self.cur: Cursor
    """

    # public:
    def __init__(self, db, usr, passwd, host="localhost"):
        """
         @database:string
         @username:string
         @password:string
         @host:string
        """
        super(MySqlDatabase, self).__init__(db, usr, passwd, host)
        self.db = pymysql.connect(
                host=host, user=usr, passwd=passwd, db=db, autocommit=True
            )
        self.cur = self.db.cursor()
        return None

    def insert(self, table_name,  **kwargs): 
        """
         @table_name:string
         @**kwargs:dict
         @validation:boolean
        """
        print(kwargs)
        key, value = kwargs.popitem()
        keys = "(`%s`" % (key)
        if type(value) == int:
            values = '(%s' % (value)
        elif type(value) == bool:
            if value:
                values = '(1'
            else:
                values = '(0'
        else:
            values = '("%s"' % (value)
        for key, value in kwargs.items():
            keys += ", `%s`" % (key)
            if type(value) == int:
                values += ', %s' % (value)
            elif type(value) == bool:
                if value:
                    values += ', 1'
                else:
                    values += ', 0'
            else:
                values += ', "%s"' % (value)
        keys += ")"
        values += ")"
        query = 'INSERT INTO `%s` %s VALUE %s' % (table_name, keys, values)
        print(query)
        response = self.cur.execute(query)
        if response:
            id = self.cur.lastrowid
            self.process.setUpdated(table_name, id)
            return id
        else:
            return False

    def update(self, table_name, id, **kwargs):
        """
         UPDATE table_name
         SET column1=value, column2=value...
         WHERE ID = 5
        """
        key, value = kwargs.popitem()
        if type(value) == int:
            query = 'UPDATE `%s` SET `%s`=%s' % (table_name, key, value)
        elif type(value) == bool:
            if value:
                query = 'UPDATE `%s` SET `%s`=1' % (table_name, key)
            else:
                query = 'UPDATE `%s` SET `%s`=0' % (table_name, key)
        else:
            query = 'UPDATE `%s` SET `%s`="%s"' % (table_name, key, value)
        for key, value in kwargs.items():
            if type(value) == int:
                query += ', `%s`=%s' % (key, value)
            elif type(value) == bool:
                if value:
                    query += ', `%s`=1' % (key)
                else:
                    query += ', `%s`=0' % (key)
            else:
                query += ', `%s`="%s"' % (key, value)
        query += ' WHERE `id` LIKE %s' % (int(id))
        # print(query)
        response = self.cur.execute(query)
        self.process.setUpdated(table_name, id)
        return response

    def delete(self, table_name, id):
        """
         DELETE FROM table_name WHERE ID LIKE id
        """
        query = "DELETE FROM `%s` WHERE `ID` LIKE %s" % (table_name, int(id))
        response = self.cur.execute(query)
        self.process.setUpdated(table_name, -id)
        return response

    def loadTable(self, table_name): 
        """
         @table_name:string
         @table:array
        """
        self.cur.execute('SELECT * FROM `%s`' % (table_name))
        row = self.cur.fetchall()
        return row

    def load(self, table_name,  id): 
        """
         @table_name:string
         @id:int
         @datensatz:row
        """
        sql = 'SELECT * FROM `%s` WHERE `id` LIKE "%s"'
        self.cur.execute(sql % (table_name, int(id)))
        row = self.cur.fetchall()
        if len(row) == 0:
            return False
        else:
            return row[0]

    def loadIdByAttr(self, table_name, attr, attr_val): 
        """
         @table_name:string
         @id:int
         @datensatz:row
        """
        sql = 'SELECT `id` FROM `%s` WHERE `%s` LIKE "%s"'
        self.cur.execute(sql % (table_name, attr, attr_val))
        row = self.cur.fetchall()
        if len(row) == 0:
            return False
        else:
            return row[0][0]

    def loadForeignKeys(
            self, table, table_id_name, join_table, join_table_id_value
            ):
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
        sql = 'SELECT `%s`.`id` FROM `%s` JOIN `%s` ON `%s`.`id` LIKE `%s`.`%s`\
                WHERE `%s`.`id` LIKE "%s"'
        query = sql % (
                table, table, join_table, join_table, table, table_id_name,
                join_table, join_table_id_value
                )
        self.cur.execute(query)
        tmp_keys = self.cur.fetchall()
        foreign_keys = []
        if tmp_keys:
            for foreign_key in tmp_keys:
                foreign_keys.append(foreign_key[0])
        return foreign_keys



