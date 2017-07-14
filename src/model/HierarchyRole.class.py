# 
from .Role import Role
class HierarchyRole ( Role ):
	#private:
	"""
	id_hierarchy_lvl # int
	"""
	
	def __init__( self, **kwargs):
		"""
		 @**kwargs:
		  id: int
		  id_hierarchy_lvl: int
		  id_permission: int
		  id_max_hierarchy_lvl: int = None
		"""
		missing="HierarchyRole __init__: Missing "
		if "id" in kwargs.keys():
			self.id=int(kwargs["id"])
		else:
			raise ValueError(missing+"id")
		if "id_hierarchy_lvl" in kwargs.keys():
			self.id_hierarchy_lvl=int(kwargs["id_hierarchy_lvl"])
		else:
			raise ValueError(missing+"id_hierarchy_lvl")
		if "id_permission" in kwargs.keys():
			self.id_permission=int(kwargs["id_permission"])
		else:
			raise ValueError(missing+"id_permission")
		if "id_max_hierarchy_lvl" in kwargs.keys():
			self.id_max_hierarchy_lvl=int(kwargs["id_max_hierarchy_lvl"])
	
	def getHierarchyLvl(self):
		"""
		 @user_id: int
		"""
		return self.id_hierarchy_lvl
