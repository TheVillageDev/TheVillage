# 
from ..Controller import Controller
from .HierarchyRoleController import HierarchyRoleController
from .HierarchyLvl import HierarchyLvl
class HierarchyLvlController ( Controller ):
	#private:
	table_name="tbl_hierarchy_lvl"
	
	#interface
	def __init__( self, process, database, **kwargs):
		"""
		 @database: Database
		 @**kwargs
		  hierarchy_role_controller:HierarchyRoleController
		"""
		super(HierarchyLvlController,self).__init__(process,database)
		if "hierarchy_role_controller" in kwargs.keys():
			self.hierarchy_role_controller=kwargs["hierarchy_role_controller"]
		else:
			self.hierarchy_role_controller=""
		#self.initiateAllFromDB()
		
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
		if item and self.hierarchy_role_controller:
			deleted=self.database.delete(self.table_name,id_item)
			if not deleted:
				validation = False
			else:
				self.itemList.remove(item)
				self.indexIdx-=1
				for id_hierarchy_role in item.getHierarchyRoles():
					self.hierarchy_role_controller.delItem(id_hierarchy_role)
				validation = True
		else:
			validation = False
		return validation
	
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
		  description: string
		"""
		if "description" in kwargs.keys():
			description=str(kwargs["description"])
			id=self.database.insert(self.table_name,description=description)
			item=HierarchyLvl(id=int(id), description=description)
			validation=self.addItem(item)
		if validation:
			return True
		else:
			return False
	
	def initiateFromDB( self, id_item ): 
		"""
		 @id_item:int
		"""
		print("hlctrl: %s"%(id_item))
		if self.hierarchy_role_controller:
			item_data=self.database.load(self.table_name,id_item)
			print(item_data)
			if item_data:
				id=int(item_data[0])
				duplicate=self.isItem(id)
				if duplicate:
					self.removeItem(id)
				description=str(item_data[1])
				table_name_hierarchy_role=self.hierarchy_role_controller.getTableName()
				#loadForeignKeys(table,table_attribut_name,join_table,join_table_attribut_name)
				hierarchy_role_ids=self.database.loadForeignKeys(table_name_hierarchy_role,"id_hierarchy_lvl",self.table_name,id)
				ids_hierarchy_role=[]
				for hierarchy_role_id in hierarchy_role_ids:
					if self.hierarchy_role_controller.getItemById(int(hierarchy_role_id)):
						ids_hierarchy_role.append(int(hierarchy_role_id))
					else:
						print("no hierarchy_role with id %s"%(hierarchy_role_id))
				item=HierarchyLvl(id=id,description=description,ids_hierarchy_role=ids_hierarchy_role)
				self.addItem(item)
				return True
			else:
				print("Hierarchy Lvl %s could not be found!"%(id_item))
				return False
		else:
			return False

	def initiateAllFromDB( self ): 
		"""
		"""
		if self.hierarchy_role_controller:
			item_datas=self.database.loadTable(self.table_name)
			for item_data in item_datas:
				id=int(item_data[0])
				duplicate=self.isItem(id)
				if duplicate:
					self.removeItem(id)
				description=str(item_data[1])
				table_name_hierarchy_role=self.hierarchy_role_controller.getTableName()
				#loadForeignKeys(table,table_attribut_name,join_table,join_table_attribut_name)
				hierarchy_role_ids=self.database.loadForeignKeys(table_name_hierarchy_role,"id_hierarchy_lvl",self.table_name,id)
				ids_hierarchy_role=[]
				for hierarchy_role_id in hierarchy_role_ids:
					if self.hierarchy_role_controller.getItemById(int(hierarchy_role_id)):
						ids_hierarchy_role.append(int(hierarchy_role_id))
					else:
						print("no hierarchy_role with id %s"%(hierarchy_role_id))
				item=HierarchyLvl(id=id,description=description,ids_hierarchy_role=ids_hierarchy_role)
				self.addItem(item)
			return True
		else:
			return False
	#end interface
	
	def getDescription( self, id_hierarchy_lvl): 
		"""
		 @id_hierarchy_lvl:int
		 @description:string
		"""
		item=self.getItemById(id_hierarchy_lvl)
		return item.getDescription()
	
	def hasPermission( self, id_hierarchy_lvl,  id_permission): 
		"""
		 @id_hierarchy_lvl:int
		 @id_permission:int
		"""
		hierarchy_lvl=self.getItemById(id_hierarchy_lvl)
		if self.hierarchy_role_controller and hierarchy_lvl:
			validation=False
			ids_hierarchy_role=hierarchy_lvl.getHierarchyRoles()
			for id_hierarchy_role in ids_hierarchy_role:
				role_permission=self.hierarchy_role_controller.getPermission(id_hierarchy_role)
				role_max_hierarchy_lvl=self.hierarchy_role_controller.getMaxHierarchyLvl(id_hierarchy_role)
				if role_permission == id_permission and not role_max_hierarchy_lvl:
					validation=True
			if validation:
				return True
			else:
				return False
		else:
			return False
	
	def hasPermissionOn( self, id_hierarchy_lvl,  id_permission,  id_on_hierarchy_lvl): 
		"""
		 @id_hierarchy_lvl:int
		 @id_permission:int
		 @id_on_hierarchy_lvl:int
		"""
		hierarchy_lvl=self.getItemById(id_hierarchy_lvl)
		if self.hierarchy_role_controller and hierarchy_lvl:
			validation=False
			ids_hierarchy_role=hierarchy_lvl.getHierarchyRoles()
			for id_hierarchy_role in ids_hierarchy_role:
				role_permission=self.hierarchy_role_controller.getPermission(id_hierarchy_role)
				role_max_hierarchy_lvl=self.hierarchy_role_controller.getMaxHierarchyLvl(id_hierarchy_role)
				if role_permission == id_permission and role_max_hierarchy_lvl <= id_on_hierarchy_lvl:
					validation=True
			if validation:
				return True
			else:
				return False
		else:
			return False	
	
	def getHighestLvl( self):
		self.initiateAllFromDB()
		highest_lvl=self.itemList[0].getId()
		for item in self.itemList:
			if item.getId() < highest_lvl:
				highest_lvl=item.getId()
		return highest_lvl
	
	def getLowestLvl( self):
		self.initiateAllFromDB()
		lowest_lvl=self.itemList[0].getId()
		for item in self.itemList:
			if item.getId() > lowest_lvl:
				lowest_lvl=item.getId()
		return lowest_lvl
	
	def setHierarchyRoleController( self, hierarchy_role_controller): 
		"""
		 @hierarchy_role_controller:HierarchyRoleController
		"""
		self.hierarchy_role_controller=hierarchy_role_controller
		return True

	def getHierarchyRoles(self,id_hierarchy_lvl):
		item=self.getItemById(id_hierarchy_lvl)
		if item:
			return item.getHierarchyRoles()
		else:
			return False
	
	def addHierarchyRole(self,id_hierarchy_lvl,id_hierarchy_role):
		item=self.getItemById(id_hierarchy_lvl)
		if item:
			validation=item.addHierarchyRole(id_hierarchy_role)
			return validation
		else:
			return False
	
	def removeHierarchyRole(self,id_hierarchy_lvl,id_hierarchy_role):
		item=self.getItemById(id_hierarchy_lvl)
		if item:
			validation=item.removeHierarchyRole(id_hierarchy_role)
			return validation
		else:
			return False
