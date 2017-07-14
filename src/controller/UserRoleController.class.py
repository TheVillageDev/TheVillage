# 
from .UserRole import UserRole
from .RoleController import RoleController
class UserRoleController ( RoleController ):

	#private:
	table_name="tbl_extra_role"
	
	#public
	#interface
	def __init__(self, process, database):
		super(UserRoleController,self).__init__(process, database)
	
	def addItem( self, item ): 
		"""
		 @item:
		"""
		duplicate=self.isItem(item.getId())
		if not duplicate:
			self.itemList.append(item)
			self.indexIdx+=1
			return True
		else:
			print("Item is a duplicate!")
			return False

	def delItem( self, id_item ): 
		"""
		 @id_item:int
		"""
		item=self.getItemById(id_item)
		if item:
			validation=self.database.delete(self.table_name,id_item)
			if not validation:
				return False
			self.itemList.remove(item)
			self.indexIdx-=1
			return True
		else:
			return False
	
	def removeItem( self, id_item ): 
		"""
		 @id_item:int
		"""
		item=self.getItemById(id_item)
		if item:
			self.itemList.remove(item)
			self.indexIdx-=1
			return True
		else:
			return False
	
	def createItem( self, **kwargs ):
		"""
		 @**kwargs:
		  id_permission:int
		  id_max_hierarchy_lvl:int = ""
		  id_user:int
		"""
		missing="UserRoleController createItem(): "
		if not "id_permission" in kwargs.keys():
			raise ValueError(missing+"id_permission")
		if not "id_user" in kwargs.keys():
			raise ValueError(missing+"id_user")
		if "id_permission" in kwargs.keys() and "id_user" in kwargs.keys():
			id_permission=int(kwargs["id_permission"])
			id_user=int(kwargs["id_user"])
			if "id_max_hierarchy_lvl" in kwargs.keys():
				id_max_hierarchy_lvl=int(kwargs["id_max_hierarchy_lvl"])
				id=self.database.insert(self.table_name,id_permission=id_permission,id_max_hierarchy_lvl=id_max_hierarchy_lvl,id_user=id_user)
				item=UserRole(id=int(id), id_permission=id_permission,id_max_hierarchy_lvl=id_max_hierarchy_lvl,id_user=id_user)
				validation=self.addItem(item)
			else:
				id=self.database.insert(self.table_name,id_permission=id_permission,id_user=id_user)
				item=UserRole(id=int(id), id_permission=id_permission,id_user=id_user)
				validation=self.addItem(item)
		if validation:
			return id
		else:
			return False
	
	def addItem( self, item ): 
		"""
		 @item:
		"""
		duplicate=self.isItem(item.getId())
		if not duplicate:
			self.itemList.append(item)
			self.indexIdx+=1
			return True
		else:
			return False

	def delItem( self, id_item ): 
		"""
		 @id_item:int
		"""
		item=self.getItemById(id_item)
		if item:
			id=item.getId()
			validation=self.database.delete(self.table_name,id)
			if not validation:
				return False
			self.itemList.remove(item)
			self.indexIdx-=1
			return True
		else:
			return False

	def initiateFromDB( self, id_item ): 
		"""
		 @id_item:int
		"""
		item_data=self.database.load(self.table_name,id_item)
		if item_data:
			print(item_data)
			id=int(item_data[0])
			duplicate=self.isItem(id)
			if duplicate:
				self.removeItem(id)
			id_permission=int(item_data[1])
			id_user=int(item_data[2])
			print(str(item_data[3]))
			if str(item_data[3]) == "None":
				item=UserRole(id=id,id_permission=id_permission,id_user=id_user)
				self.addItem(item)
			else:
				id_max_hierarchy_lvl=int(item_data[3])
				item=UserRole(id=id,id_permission=id_permission,id_user=id_user,id_max_hierarchy_lvl=id_max_hierarchy_lvl)
				self.addItem(item)
			return True
		else:
			return False

	def initiateAllFromDB( self ): 
		"""
		"""
		item_datas=self.database.loadTable(self.table_name)
		for item_data in item_datas:
			id=int(item_data[0])
			duplicate=self.isItem(id)
			if duplicate:
				self.removeItem(id)
			id_permission=int(item_data[1])
			id_user=int(item_data[2])
			if str(item_data[3]) == "None":
				item=UserRole(id=id,id_permission=id_permission,id_user=id_user)
				self.addItem(item)
			else:
				id_max_hierarchy_lvl=int(item_data[3])
				item=UserRole(id=id,id_permission=id_permission,id_user=id_user,id_max_hierarchy_lvl=id_max_hierarchy_lvl)
				self.addItem(item)
		return True
	#end interface
	
	#public:
	def getUser( self, id_role): 
		"""
		 @id_role:int
		 @id_max_hierarchy_lvl:int
		"""
		item=self.getItemById(id_role)
		return item.getUser()


