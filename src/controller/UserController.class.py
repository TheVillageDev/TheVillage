# 
from ..Controller import Controller
from .User import User
from .UserRoleController import UserRoleController
from .HierarchyLvlController import HierarchyLvlController
#from ProgramController import ProgramController
#from DeviceGroupController import DeviceGroupController
#from DeviceController import DeviceController
class UserController ( Controller ):
	"""
	 @author: Marco Schlicht
	 @netteberatung: Lara Klein
	"""
	#private:
	table_name="tbl_usr"
	
	def __init__( self, process, database, **kwargs):
		"""
		 @database: Database
		 @**kwargs
		  user_role_controller: UserRoleController
		  hierarchy_lvl_controller: HierarchyLvlController
		  program_controller: ProgramController
		  device_group_controller: DeviceGroupController
		  device_controller: DeviceController
		"""
		super(UserController,self).__init__(process,database)
		if "user_role_controller" in kwargs.keys():
			self.user_role_controller=kwargs["user_role_controller"]
		else:
			self.user_role_controller=""
		if "hierarchy_lvl_controller" in kwargs.keys():
			self.hierarchy_lvl_controller=kwargs["hierarchy_lvl_controller"]
		else:
			self.hierarchy_lvl_controller=""
		if "program_controller" in kwargs.keys():
			self.program_controller=kwargs["program_controller"]
		else:
			self.program_controller=""
		if "device_group_controller" in kwargs.keys():
			self.device_group_controller=kwargs["device_group_controller"]
		else:
			self.device_group_controller=""
		if "device_controller" in kwargs.keys():
			self.device_controller=kwargs["device_controller"]
		else:
			self.device_controller=""
		#self.initiateAllFromDB()

	def createItem(self,**kwargs):
		"""
		 @**kwargs:
		  username:string
		  password:string
		  email:string
		"""
		missing="UserController createItem: Missing "
		params={}
		params["id_hierarchy_lvl"]=4
		if "username" in kwargs.keys():
			params["username"]=kwargs["username"]
		else:
			raise ValueError(missing+"username")
		if "password" in kwargs.keys():
			params["password"]=kwargs["password"]
		else:
			raise ValueError(missing+"password")
		if "email" in kwargs.keys():
			params["email"]=kwargs["email"]
		else:
			raise ValueError(missing+"email")
		
		duplicate=self.getUserByUsername(params["username"])
		if not duplicate:
			params["id"]=self.database.insert(self.table_name,**params)
			item=User(**params)
			validation=self.addItem(item)
			if validation:
				return item.getId()
			else:
				return False
		else:
			raise Exception("Username is already taken.")

	def delItem( self, session_id, id_item ): 
		"""
		 @id_item:int
		"""
		perm="user.deleteUsr"
		perm_id=2
		item=self.getItemById(id_item)
		eingeloggter_user=self.getEingeloggterUser(session_id)
		if not item:
			raise Exception("No User with id=%s"%(item.getId()))
		if not eingeloggter_user:
			raise Exception("You must be logged in to Delete Users")
		has_permission=self.selfHasPermissionOn(session_id, perm_id, item.getHierarchyLvl())
		delete_me=self.getEingeloggterUser(session_id) == id_item
		if has_permission or delete_me :
			validation=self.database.delete(self.table_name,id_item)
			if not validation:
				return False
			self.itemList.remove(item)
			self.indexIdx-=1
			return True
		else:
			raise Exception("No Permission to delete User %s (id=%s)"%(item.getUsername(),item.getId()))
	
	def initiateFromDB( self, id_item ): 
		"""
		 @id_item:int
		"""
		if self.hierarchy_lvl_controller and self.user_role_controller:
			item_data=self.database.load(self.table_name,id_item)
			if item_data:
				params={}
				params["id"]=int(item_data[0])
				duplicate=self.isItem(id)
				if duplicate:
					self.removeItem(id)
				params["username"]=str(item_data[1])
				params["password"]=str(item_data[2])
				params["email"]=str(item_data[3])
				params["id_hierarchy_lvl"]=int(item_data[4])
				
				table_name_user_role=self.user_role_controller.getTableName()
				#loadForeignKeys(table,table_attribut_name,join_table,join_table_attribut_name)
				user_role_ids=self.database.loadForeignKeys(table_name_user_role,"id_user",self.table_name,params["id"])
				params["ids_user_role"]=[]
				for user_role_id in user_role_ids:
					if self.user_role_controller.getItemById(int(user_role_id)):
						params["ids_user_role"].append(int(user_role_id))
					else:
						print("no user_role with id %s"%(user_role_id))
				
				if self.hierarchy_lvl_controller.getItemById(params["id_hierarchy_lvl"]):
					item=User(**params)
					self.addItem(item)
					return True
				else:
					return False
			else:
				return False
		else:
			return False

	def initiateAllFromDB( self ): 
		"""
		"""
		if self.hierarchy_lvl_controller and self.user_role_controller:
			item_datas=self.database.loadTable(self.table_name)
			for item_data in item_datas:
				params={}
				params["id"]=int(item_data[0])
				duplicate=self.isItem(id)
				if duplicate:
					self.removeItem(id)
				params["username"]=str(item_data[1])
				params["password"]=str(item_data[2])
				params["email"]=str(item_data[3])
				params["id_hierarchy_lvl"]=int(item_data[4])
				
				table_name_user_role=self.user_role_controller.getTableName()
				#loadForeignKeys(table,table_attribut_name,join_table,join_table_attribut_name)
				user_role_ids=self.database.loadForeignKeys(table_name_user_role,"id_user",self.table_name,params["id"])
				params["ids_user_role"]=[]
				for user_role_id in user_role_ids:
					if self.user_role_controller.getItemById(int(user_role_id)):
						params["ids_user_role"].append(int(user_role_id))
					else:
						print("no user_role with id %s"%(user_role_id))
				
				valid_hierarchy_lvl=self.hierarchy_lvl_controller.getItemById(params["id_hierarchy_lvl"])
				if valid_hierarchy_lvl:
					item=User(**params)
					self.addItem(item)
				else:
					return False
			return True
		else:
			return False
	#end interface
	
	#public:
	def getUserByUsername(self, username):
		"""
		 @username:string
		"""
		user=False
		for item in self.itemList:
			if item.getUsername() == username:
				user=item
		if user:
			return user
		else:
			id_user=self.database.loadIdByAttr(self.table_name,"username",username)
			if id_user:
				user=self.getItemById(id_user)
				return user
			else:
				return False
		
	def getUserBySessionId(self, session_id):
		"""
		 @session_id:int
		"""
		if not session_id:
			return False
		user=False
		for item in self.itemList:
			if item.getSessionId() == session_id:
				user=item
		if user:
			return user
		else:
			return False
		
	def getEingeloggterUser( self, session_id): 
		"""
		 @eingeloggter_user:User
		"""
		user=self.getUserBySessionId(session_id)
		if user:
			return user.getId()
		else:
			return False

	def login( self, username,  password): 
		"""
		 @username:string
		 @password:string
		"""
		user=self.getUserByUsername(username)
		if user:
			session_id=user.startSession(password)
			return session_id
		else:
			print("Wrong Username")
			return False

	def logout( self, session_id): 
		"""
		"""
		user=self.getUserBySessionId(session_id)
		if user:
			user.stopSession()
			return True
		else:
			return False

	def getUsername( self, id_user): 
		"""
		 @id_user:int
		 @username:string
		"""
		item=self.getItemById(id_user)
		if item:
			return item.getUsername()
		else:
			return False

	def setUsername( self, session_id, id_user,  username): 
		"""
		 @id_user:int
		 @username:string
		"""
		item=self.getItemById(id_user)
		duplicate=self.getUserByUsername(username)
		if item and not duplicate:
			id_eingeloggter_user=self.getEingeloggterUser(session_id)
			if not id_eingeloggter_user:
				raise Exception("You must be logged in to set Username")
			if id_eingeloggter_user == id_user:
				validation=item.setUsername(username)
				if validation:
					validation=self.database.update(self.table_name,id_user,username=username)
					self.process.setUpdated(self.table_name,id_user)
					return validation
				else:
					return False
				return validation
			else:
				raise Exception("No Permission to change Username on User %s (id=%s)"%(item.getUsername(),item.getId()))
		else:
			return False

	def getEmail( self, id_user): 
		"""
		 @id_user:int
		 @email:string
		"""
		item=self.getItemById(id_user)
		if item:
			return item.getEmail()
		else:
			return False

	def setEmail( self, session_id, id_user,  email): 
		"""
		 @id_user:int
		 @email:string
		"""
		item=self.getItemById(id_user)
		if item:
			id_eingeloggter_user=self.getEingeloggterUser(session_id)
			if not id_eingeloggter_user:
				raise Exception("You must be logged in to set Email")
			if id_eingeloggter_user == id_user:
				validation=item.setEmail(email)
				if validation:
					validation=self.database.update(self.table_name,id_user,email=email)
					return validation
				else:
					return False
				return validation
			else:
				raise Exception("No Permission to change Email on User %s (id=%s)"%(item.getUsername(),item.getId()))
		else:
			return False

	def checkPassword( self, id_user, password): 
		"""
		 @id_user:int
		 @password:string
		"""
		item=self.getItemById(id_user)
		if item:
			validation=item.checkPassword(password)
			return validation
		else:
			return False

	def changePassword( self, id_user, old_password, new_password): 
		"""
		 @id_user:int
		 @old_password:string
		 @new_password:string
		"""
		item=self.getItemById(id_user)
		if item:
			validation=item.changePassword(new_password)
			if validation:
				validation=self.database.update(self.table_name,id_user,password=new_password)
				return validation
			else:
				return False
		else:
			return False

	def resetPassword( self, session_id, id_user): 
		"""
		 @id_user:int
		"""
		perm="user.resetPwd"
		perm_id=1
		item=self.getItemById(id_user)
		if item:
			if self.selfHasPermissionOn(session_id, perm_id, item.getHierarchyLvl()):
				#new_password=getRandInt()
				#sendPasswordPerMail()
				validation=item.changePassword("")
				if validation:
					validation=self.database.update(self.table_name,id_user,password="")
					return validation
				else:
					return False
			else:
				raise Exception("No Permission to reset Password on User %s (id=%s)"%(item.getUsername(),item.getId()))
		else:
			return False

	def getHierarchyLvl( self, id_user): 
		"""
		 @id_user:int
		 @hierarchy_roles:array
		"""
		item=self.getItemById(id_user)
		if item:
			return item.getHierarchyLvl()
		else:
			return False

	def upgrade( self, session_id, id_user): 
		"""
		 @id_user:int
		"""
		perm="hierarchyLvl.upgrade"
		perm_id=18
		item=self.getItemById(id_user)
		if item and self.hierarchy_lvl_controller:
			if self.selfHasPermissionOn(session_id, perm_id, item.getHierarchyLvl()):
				id_hierarchy_lvl=item.getHierarchyLvl()
				highest_lvl=self.hierarchy_lvl_controller.getHighestLvl()
				if id_hierarchy_lvl > highest_lvl:
					item.upgrade()
					validation=self.database.update(self.table_name,id_user,id_hierarchy_lvl=item.getHierarchyLvl())
					return validation
				else:
					return False
			else:
				raise Exception("No Permission to upgrade User %s (id=%s)"%(item.getUsername(),item.getId()))
		else:
			return False

	def downgrade( self, session_id, id_user): 
		"""
		 @id_user:int
		"""
		perm="hierarchyLvl.downgrade"
		perm_id=19
		item=self.getItemById(id_user)
		if item and self.hierarchy_lvl_controller:
			if self.selfHasPermissionOn(session_id, perm_id, item.getHierarchyLvl()):
				id_hierarchy_lvl=item.getHierarchyLvl()
				lowest_lvl=self.hierarchy_lvl_controller.getLowestLvl()
				if id_hierarchy_lvl < lowest_lvl:
					item.downgrade()
					validation=self.database.update(self.table_name,id_user,id_hierarchy_lvl=item.getHierarchyLvl())
					return validation
				else:
					return False
			else:
				raise Exception("No Permission to upgrade User %s (id=%s)"%(item.getUsername(),item.getId()))
		else:
			return False

	def getUserRoles( self, id_user): 
		"""
		 @id_user:int
		 @user_roles:array
		"""
		item=self.getItemById(id_user)
		if item:
			user_roles=item.getUserRoles()
			return user_roles
		else:
			return False

	def addUserRole( self, session_id, id_user,  id_user_role): 
		"""
		 @id_user:int
		 @id_user_role:int
		"""
		perm="extraPermission.dealWithPermissions"
		perm_id=20
		item=self.getItemById(id_user)
		if not item:
			raise Exception("No User with ID=%s"%(id_user))
		if not self.user_role_controller:
			raise Exception("Can't access UserRoleController")
		if self.selfHasPermissionOn(session_id, perm_id, item.getHierarchyLvl()):
			validation=self.user_role_controller.getItemById(id_user_role)
			if validation:
				return item.addUserRole(id_user_role)
			else:
				return False
		else:
			raise Exception("No Permission to deal with extra permissions on User %s (id=%s)"%(item.getUsername(),item.getId()))
	
	def createUserRole( self, session_id, id_user, **kwargs):
		"""
		 @session_id:string
		 @id_user:int
		 @kwargs:
		  id_permission:int
		  id_max_hierarchy_lvl:int = ""
		"""
		perm="extraPermission.dealWithPermissions"
		perm_id=20
		item=self.getItemById(id_user)
		if not item:
			raise Exception("No User with ID=%s"%(id_user))
		if not self.user_role_controller:
			raise Exception("Can't access UserRoleController")
		
		if self.selfHasPermissionOn(session_id, perm_id, item.getHierarchyLvl()):
			params={}
			params["id_user"]=id_user
			if "id_permission" in kwargs.keys():
				params["id_permission"]=kwargs["id_permission"]
			if "id_max_hierarchy_lvl" in kwargs.keys():
				params["id_max_hierarchy_lvl"]=kwargs["id_max_hierarchy_lvl"]
			id_role=self.user_role_controller.createItem(**params)
			if id_role:
				validation=self.addUserRole(session_id,id_user,id_role)
				return validation
			else:
				return False
		else:
			raise Exception("No Permission to deal with extra permissions on User %s (id=%s)"%(item.getUsername(),item.getId()))
				
		
	def removeUserRole( self, id_user,  id_user_role): 
		"""
		 @id_user:int
		 @id_user_role:int
		"""
		item=self.getItemById(id_user)
		if item:
			return item.removeUserRole(id_user_role)
		else:
			return False

	def delUserRole( self, session_id, id_user, id_user_role):
		"""
		 @id_user:int
		 @id_user_role:int
		"""
		perm="extraPermission.dealWithPermissions"
		perm_id=20
		item=self.getItemById(id_user)
		if item and self.user_role_controller:
			if self.selfHasPermissionOn(session_id, perm_id, item.getHierarchyLvl()):
				validation=item.removeUserRole(id_user_role)
				if validation:
					deleted = self.user_role_controller.delItem(id_user_role)
					if deleted:
						return True
					else:
						self.user_role_controller.initiateFromDB(id_user_role)
						return False
				else:
					return False
			else:
				raise Exception("No Permission to deal with extra permissions on User %s (id=%s)"%(item.getUsername(),item.getId()))
		else:
			return False

	def hasPermission( self, id_user,  id_permission): 
		"""
		 @id_user:int
		 @id_permission:int
		"""
		user=self.getItemById(id_user)
		if self.hierarchy_lvl_controller and user:
			has_hierarchy_lvl_perm=self.hierarchy_lvl_controller.hasPermission(user.getHierarchyLvl(),id_permission)
			if has_hierarchy_lvl_perm:
				return True
			elif self.user_role_controller:
				ids_user_role=user.getUserRoles()
				validation=False
				for id_user_role in ids_user_role:
					role_permission=self.user_role_controller.getPermission(id_user_role)
					role_max_hierarchy_lvl=self.user_role_controller.getMaxHierarchyLvl(id_user_role)
					if role_permission == id_permission and not role_max_hierarchy_lvl:
						validation=True
				if validation:
					return True
				else:
					return False
			else:
				return False
		else:
			return False

	def hasPermissionOn( self, id_user,  id_permission,  id_on_hierarchy_lvl): 
		"""
		 @id_user:int
		 @id_permission:int
		 @id_hierarchy_lvl:int
		"""
		user=self.getItemById(id_user)
		if self.hierarchy_lvl_controller and user:
			has_hierarchy_lvl_perm=self.hierarchy_lvl_controller.hasPermissionOn(user.getHierarchyLvl(),id_permission,id_on_hierarchy_lvl)
			if has_hierarchy_lvl_perm:
				return True
			elif self.user_role_controller:
				ids_user_role=user.getUserRoles()
				validation=False
				for id_user_role in ids_user_role:
					role_permission=self.user_role_controller.getPermission(id_user_role)
					role_max_hierarchy_lvl=self.user_role_controller.getMaxHierarchyLvl(id_user_role)
					if role_permission == id_permission and role_max_hierarchy_lvl <= id_on_hierarchy_lvl:
						validation=True
				if validation:
					return True
				else:
					return False
		else:
			return False

	def selfHasPermission( self, session_id, id_permission):
		id_user=self.getEingeloggterUser(session_id)
		if id_user:
			validation=self.hasPermission(id_user,id_permission)
			return validation
		else:
			print("User is not logged in!")
			return False
	
	def selfHasPermissionOn( self, session_id, id_permission, id_on_hierarchy_lvl):
		id_user=self.getEingeloggterUser(session_id)
		if id_user:
			validation=self.hasPermissionOn(id_user,id_permission,id_on_hierarchy_lvl)
			return validation
		else:
			print("User is not logged in!")
			return False
	
	def getPrivateDeviceGroups( self, session_id, id_user): 
		"""
		 @id_user:int
		 @private_device_groups:array
		"""
		perm="privateGroup.seeGrp"
		perm_id="9"
		item=self.getItemById(id_user)
		eingeloggter_user=self.getEingeloggterUser(session_id)
		if item and self.device_group_controller:
			if self.selfHasPermissionOn( session_id, perm_id, item.getHierarchyLvl()) or eingeloggter_user == id_item:
				ids_device_groups=item.getAllDeviceGroups()
				ids_private_device_group=[]
				for id_device_group in ids_device_group:
					private=device_group_controller.isPrivate(id_device_group)
					if private:
						ids_private_device_group.append(id_device_group)
				return ids_private_device_group
			else:
				raise Exception("No Permission to get private Device Groups on User %s (id=%s)"%(item.getUsername(),item.getId()))
		else:
			return False

	def getGlobalDeviceGroups( self, id_user): 
		"""
		 @id_user:int
		 @global_device_groups:array
		"""
		item=self.getItemById(id_user)
		if item and self.device_group_controller:
			ids_device_groups=item.getAllDeviceGroups()
			ids_global_device_group=[]
			for id_device_group in ids_device_group:
				private=device_group_controller.isPrivate(id_device_group)
				if not private:
					ids_global_group.append(id_device_group)
			return ids_global_device_group
		else:
			return False

	def addDeviceGroup( self, session_id, id_user, id_device_group): 
		"""
		 @id_user:int
		 @id_device_group:int
		"""
		perm_private="privateGroup.createGrp"
		perm_id_private=6
		perm_global="globalGroup.createGrp"
		perm_id_global=3
		item=self.getItemById(id_user)
		if item and self.device_group_controller:
			if (self.device_group_controller.isPrivate() and self.selfHasPermissionOn(session_id, perm_id_private, item.getHierarchyLvl())) \
			   or (not self.device_group_controller.isPrivate() and self.selfHasPermissionOn(session_id, perm_id_global, item.getHierarchyLvl())):
				validation=self.device_group_controller.getItemById(id_user_role)
				if validation:
					return item.addDeviceGroup(id_user_role)
				else:
					return False
			else:
				raise Exception("No Permission to add DeviceGroup id=%s"%(id_device_group))
		else:
			return False

	def removeDeviceGroup( self, id_user, id_device_group): 
		"""
		 @id_user:int
		 @id_device_group:int
		"""
		item=self.getItemById(id_user)
		if item:
			return item.removeDeviceGroup(id_user_role)
		else:
			return False
		
	def delDeviceGroup( self, session_id, id_user, id_device_group): 
		"""
		 @id_user:int
		 @id_device_group:int
		"""
		perm_private="privateGroup.deleteGrp"
		perm_id_private=8
		perm_global="globalGroup.deleteGrp"
		perm_id_global=5
		item=self.getItemById(id_user)
		if item and self.device_group_controller:
			if (self.device_group_controller.isPrivate() and self.selfHasPermissionOn(session_id, perm_id_private, item.getHierarchyLvl())) \
			   or (not self.device_group_controller.isPrivate() and self.selfHasPermissionOn(session_id, perm_id_global, item.getHierarchyLvl())):
				validation=item.removeDeviceGroup(id_user_role)
				if validation:
					deleted = self.device_group_controller.delItem(id_user_role)
					if deleted:
						return True
					else:
						self.device_group_controller.initiateFromDB(id_user_role)
						return False
				else:
					return False
			else:
				raise Exception("No Permission to delete DeviceGroup id=%s"%(id_device_group))
		else:
			return False

	'''
	def getDevices( self, id_user): 
		"""
		 @id_user:int
		 @devices:array
		"""
		item=self.getItemById(id_user)
		if item:
			return item.getDevices()
		else:
			return False

	def addDevice( self, session_id, id_user,  id_device): 
		"""
		 @id_user:int
		 @id_device:int
		"""
		perm="device.createDev"
		perm_id=10
		item=self.getItemById(id_user)
		if item and self.device_controller:
			if self.selfHasPermissionOn(session_id, perm_id, item.getHierarchyLvl()):
				validation=self.device_controller.getItemById(id_user_role)
				if validation:
					return item.addDevice(id_user_role)
				else:
					return False
			else:
				raise Exception("No Permission to add Device on User %s (id=%s)"%(item.getUsername(),item.getId()))
		else:
			return False

	def removeDevice( self, id_user,  id_device): 
		"""
		 @id_user:int
		 @id_device:int
		"""
		item=self.getItemById(id_user)
		if item and self.device_controller:
			validation=self.device_controller.getItemById(id_user_role)
			if validation:
				return item.addDevice(id_user_role)
			else:
				return False
		else:
			return False

	def delDevice( self, session_id, id_user,  id_device): 
		"""
		 @id_user:int
		 @id_device:int
		"""
		perm="device.deleteDev"
		perm_id=13
		item=self.getItemById(id_user)
		if item and self.device_controller:
			if self.selfHasPermissionOn(session_id, perm_id, item.getHierarchyLvl()):
				validation=item.removeDevice(id_user_role)
				if validation:
					deleted = self.device_controller.delItem(id_user_role)
					if deleted:
						return True
					else:
						self.device_controller.initiateFromDB(id_user_role)
						return False
				else:
					return False
			else:
				raise Exception("No Permission to delete Device on User %s (id=%s)"%(item.getUsername(),item.getId()))
		else:
			return False
	'''

	'''
	def getPrograms( self, id_user): 
		"""
		 @id_user:int
		 @programs:array
		"""
		item=self.getItemById(id_user)
		if item:
			return item.getPrograms()
		else:
			return False

	def addProgram( self, id_user,  id_program): 
		"""
		 @id_user:int
		 @id_program:int
		"""
		item=self.getItemById(id_user)
		if item and self.program_controller:
			validation=self.program_controller.getItemById(id_user_role)
			if validation:
				return item.addProgram(id_user_role)
			else:
				return False
		else:
			return False

	def removeProgram( self, id_user,  id_program): 
		"""
		 @id_user:int
		 @id_program:int
		"""
		item=self.getItemById(id_user)
		if item:
			return item.removeProgram(id_user_role)
		else:
			return False

	def delProgram( self, id_user,  id_program): 
		"""
		 @id_user:int
		 @id_program:int
		"""
		item=self.getItemById(id_user)
		if item and self.program_controller:
			validation=item.removeProgram(id_user_role)
			if validation:
				deleted = self.program_controller.delItem(id_user_role)
				if deleted:
					return True
				else:
					self.program_controller.initiateFromDB(id_user_role)
					return False
			else:
				return False
		else:
			return False
	'''
	
	def setUserRoleController( self, user_role_controller): 
		"""
		 @user_role_controller:UserRoleController
		"""
		self.user_role_controller = user_role_controller
		return True

	def setHierarchyLvlController( self, hierarchy_lvl_controller): 
		"""
		 @hierarchy_lvl_controller:HierarchyLvlController
		"""
		self.hierarchy_lvl_controller = hierarchy_lvl_controller
		return True

	def setProgramController( self, program_controller): 
		"""
		 @program_controller:ProgramController
		"""
		self.program_controller = program_controller
		return True

	def setDeviceGroupController( self, device_group_controller): 
		"""
		 @device_group_controller:DeviceGroupController
		"""
		self.device_group_controller = device_group_controller
		return True

	def setDeviceController( self, device_controller): 
		"""
		 @device_controller:DeviceController
		"""
		self.device_controller = device_controller
		return True

	def listUsers(self):
		#self.initiateAllFromDB()
		for u in self.getAllItems():
		  print("%s - %s (%s)"%(u.getId(),u.getUsername(),self.hierarchy_lvl_controller.getDescription(u.getHierarchyLvl())))


