# 
from abc import ABCMeta, abstractmethod
from ..Controller import Controller
class RoleController ( Controller, metaclass=ABCMeta ):
	#protected:
	"""
	permission_controller # PermissionController
	hierarchy_lvl_controller # HierarchyLvlController
	"""
	
	#public:
	def getPermission( self, id_role): 
		"""
		 @id_role:int
		 @id_permission:int
		"""
		item=self.getItemById(id_role)
		return item.getPermission()

	def getMaxHierarchyLvl( self, id_role): 
		"""
		 @id_role:int
		 @id_max_hierarchy_lvl:int
		"""
		item=self.getItemById(id_role)
		return item.getMaxHierarchyLvl()

	def setPermissionController( self, permission_controller): 
		"""
		 @permission_controller:PermissionController
		"""
		self.permission_controller=permission_controller
		return True

	def setHierarchyLvlController( self, hierarchy_lvl_controller): 
		"""
		 @hierarchy_lvl_controller:HierarchyLvlController
		"""
		self.hierarchy_lvl_controller=hierarchy_lvl_controller
		return True


