# 
from uuid import uuid4
from time import time
class User (  ):
	#private:
	"""
	id # int
	username # string
	__password # string
	email # string
	session_id # string
	timestamp # time
	timestamp_delay # int
	id_hierarchy_lvl # int
	ids_user_role # array
	ids_device_group # array
	ids_device # array
	ids_program # array
	"""
	def __init__(self,**kwargs):
		"""
		 @**kwargs:
		  id: int
		  username: string  
		  __password: string
		  email: string
		  id_hierarchy_lvl: int
		  ids_user_role: array = []
		  ids_device_group: array = []
		  ids_device: array = []
		  ids_program: array = []
		"""
		missing="User __init__: Missing "
		self.session_id=""
		self.timestamp=0
		self.timestamp_delay=0
		if "id" in kwargs.keys():
			self.id=int(kwargs["id"])
		else:
			raise ValueError(missing+"id")
		if "username" in kwargs.keys():
			self.username=str(kwargs["username"])
		else:
			raise ValueError(missing+"username")
		if "password" in kwargs.keys():
			self.__password=str(kwargs["password"])
		else:
			raise ValueError(missing+"password")
		if "email" in kwargs.keys():
			self.email=str(kwargs["email"])
		else:
			raise ValueError(missing+"email")
		if "id_hierarchy_lvl" in kwargs.keys():
			self.id_hierarchy_lvl=int(kwargs["id_hierarchy_lvl"])
		else:
			raise ValueError(missing+"id_hierarchy_lvl")
		if "ids_user_role" in kwargs.keys():
			self.ids_user_role=list(kwargs["ids_user_role"])
		else:
			self.ids_user_role=[]
		if "ids_device_group" in kwargs.keys():
			self.ids_device_group=list(kwargs["ids_device_group"])
		else:
			self.ids_device_group=[]
		if "ids_device" in kwargs.keys():
			self.ids_device=list(kwargs["ids_device"])
		else:
			self.ids_device=[]
		if "ids_program" in kwargs.keys():
			self.ids_program=list(kwargs["ids_program"])
		else:
			self.ids_program=[]

	#public:
	def getId( self):
		"""
		 @id:int
		"""
		return self.id

	def getUsername( self): 
		"""
		 @username:string
		"""
		return self.username

	def setUsername( self, new_username): 
		"""
		 @new_username:string
		"""
		self.username=str(new_username)
		return True

	def getEmail( self): 
		"""
		 @email:string
		"""
		return self.email

	def setEmail( self, new_email): 
		"""
		 @new_email:string
		"""
		self.email=str(new_email)
		return True

	def checkPassword( self, password): 
		"""
		 @password:string
		"""
		if self.__password == password:
			return True
		else:
			return False

	def changePassword( self, new_password): 
		"""
		 @old_password:string
		"""
		self.__password=str(new_password)
		return True

	def getTimestamp(self):
		return self.timestamp
		
	def getTimestampDelay(self):
		return self.timestamp_delay

	def getSessionId( self):
		if self.getTimestamp()+self.getTimestampDelay() == 0:
			return False
		elif self.getTimestamp()+self.getTimestampDelay() < time():
			self.timestamp=0
			self.timestamp_delay=0
			print("Deine Session ist abgelaufen!")
			return False
		else:
			return self.session_id

	def startSession( self, password):
		validation=self.checkPassword(password)
		if validation:
			self.session_id=str(uuid4())
			self.timestamp=time()
			#4h in seconds
			self.timestamp_delay=4*60*60
			return self.session_id
		else:
			print("wrong password")
			return False

	def stopSession( self):
		self.session_id=""
		self.timestamp=0
		#4h in seconds
		self.timestamp_delay=0
		return True
	
	def getHierarchyLvl( self): 
		"""
		 @hierarchy_roles:
		"""
		return self.id_hierarchy_lvl

	def upgrade( self): 
		"""
		"""
		self.id_hierarchy_lvl-=1
		return True

	def downgrade( self): 
		"""
		"""
		self.id_hierarchy_lvl+=1
		return True

	def getUserRoles( self): 
		"""
		 @user_roles:array
		"""
		return self.ids_user_role

	def addUserRole( self, id_user_role): 
		"""
		 @id_user:int
		"""
		if int(id_user_role) in self.ids_user_role:
			return False
		else:
			self.ids_user_role.append(int(id_user_role))
			return True

	def removeUserRole( self, id_user_role): 
		"""
		 @id_user:int
		"""
		if int(id_user_role) in self.ids_user_role:
			self.ids_user_role.remove(int(id_user_role))
			return True
		else:
			return False

	def getAllDeviceGroups( self): 
		"""
		 @all_device_groups:array
		"""
		return self.ids_device_group

	def addDeviceGroup( self, id_device_group): 
		"""
		 @id_device_group:int
		"""
		if int(id_device_group) in self.ids_device_group:
			return False
		else:
			self.ids_device_group.append(int(id_device_group))
			return True

	def removeDeviceGroup( self, id_device_group ): 
		"""
		 @id_device_group:int
		 @validation :boolean
		"""
		if int(id_device_group) in self.ids_device_group:
			self.ids_device_group.remove(int(id_device_group))
			return True
		else:
			return False

	def getDevices( self): 
		"""
		 @devices:array
		"""
		return self.ids_device

	def addDevice( self, id_device): 
		"""
		 @id_device:int
		"""
		if int(id_device) in self.ids_device:
			return False
		else:
			self.ids_device.append(int(id_device))
			return True

	def removeDevice( self, id_device): 
		"""
		 @id_device:int
		"""
		if int(id_device) in self.ids_device:
			self.ids_device.remove(int(id_device))
			return True
		else:
			return False

	def getPrograms( self): 
		"""
		 @programs:array
		"""
		return self.ids_program

	def addProgram( self, id_program):
		"""
		 @id_program:int
		"""
		if int(id_program) in self.ids_program:
			return False
		else:
			self.ids_program.append(int(id_program))
			return True

	def removeProgram( self, id_program): 
		"""
		 @id_program:int
		"""
		if int(id_program) in self.ids_program:
			self.ids_program.remove(int(id_program))
			return True
		else:
			return False


