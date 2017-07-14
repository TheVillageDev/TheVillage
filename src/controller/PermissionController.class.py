# 
from ..Controller import Controller
from .Permission import Permission
class PermissionController ( Controller ):

	#private:
	table_name="tbl_permission"
	process_name="Permission"
	
	#interface:
	#public:
	def __init__(self, process, database):
		super(PermissionController,self).__init__(process, database)
		self.initiateAllFromDB()
	
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
	
	def createItem( self, description ):
		id=self.database.insert(self.table_name,description=str(description))
		item=Permission(id=int(id), description=str(description))
		validation=self.addItem(item)
		if validation:
			return True
		else:
			return False

	def initiateFromDB( self, id_item ): 
		"""
		 @id_item:int
		"""
		item_data=self.database.load(self.table_name,id_item)
		if item_data:
			#print(item_data)
			id=item_data[0]
			duplicate=self.isItem(id)
			if duplicate:
				self.removeItem(id)
			description=item_data[1]
			item=Permission(id=int(id),description=str(description))
			self.addItem(item)
			return True
		else:
			return False

	def initiateAllFromDB( self ): 
		"""
		"""
		item_datas=self.database.loadTable(self.table_name)
		#print(item_datas)
		for item_data in item_datas:
			id=item_data[0]
			duplicate=self.isItem(id)
			if duplicate:
				self.removeItem(id)
			description=item_data[1]
			item=Permission(id=int(id),description=str(description))
			self.addItem(item)
		return True
	
	#end interface
	
	#public:

	def getIdByDescription( self, description): 
		"""
		 @description:string
		 @id_permission:int
		"""
		for item in self.itemList:
			if item.getDescription() == description:
				id_permission = item.getId()
				return id_permission
		return False

	def getDescription( self, id_permission): 
		"""
		 @id_permission:int
		 @description:string
		"""
		item=self.getItemById(id_permission)
		if item:
			description=item.getDescription()
			return description
		return False

	def listPermissions(self ):
		for p in self.getAllItems():
		  print("%s - %s"%(p.getId(),p.getDescription()))

