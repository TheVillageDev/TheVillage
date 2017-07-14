from .Process import Process
from .MySqlDatabase import MySqlDatabase
from .server.PermissionController import PermissionController
from .server.HierarchyRoleController import HierarchyRoleController
from .server.HierarchyLvlController import HierarchyLvlController
from .server.UserRoleController import UserRoleController
from .server.UserController import UserController
from .server.BwlListUserController import BwlListUserController
from .server.BwlListController import BwlListController
from .server.DeviceController import DeviceController
from .server.ClientController import ClientController

class ServerApp(object):
    def __init__(self, **kwargs):
        """
         @**kwargs:
          DB_USERNAME:string
          DB_PASSWORD:string
        """
        params={}
        if "DB_USERNAME" in kwargs.keys():
            params["DB_USERNAME"]=kwargs["DB_USERNAME"]
        else:
            raise KeyError("ServerApp: __init__: missing keyword DB_USERNAME")
        if "DB_PASSWORD" in kwargs.keys():
            params["DB_PASSWORD"]=kwargs["DB_PASSWORD"]
        else:
            raise KeyError("ServerApp: __init__: missing keyword DB_PASSWORD")
        print("Initiating new server application")
        proc=Process()
        db=MySqlDatabase(proc,"shp_server",params["DB_USERNAME"],params["DB_PASSWORD"])
        pctrl=PermissionController(proc,db)
        hrctrl=HierarchyRoleController(proc,db)
        hlctrl=HierarchyLvlController(proc,db,hierarchy_role_controller=hrctrl)
        urctrl=UserRoleController(proc,db)
        usrctrl=UserController(proc,db,hierarchy_lvl_controller=hlctrl,user_role_controller=urctrl)
        cctrl=ClientController(proc,db,user_controller=usrctrl)
        devctrl=DeviceController(proc,db,user_controller=usrctrl,client_controller=cctrl)
        hrctrl.initiateAllFromDB()
        hlctrl.initiateAllFromDB()
        urctrl.initiateAllFromDB()
        usrctrl.initiateAllFromDB()
        devctrl.initiateAllFromDB()
        self.proc=proc
        self.db=db
        self.pctrl=pctrl
        self.hrctrl=hrctrl
        self.hlctrl=hlctrl
        self.urctrl=urctrl
        self.usrctrl=usrctrl
        self.devctrl=devctrl
        self.cctrl=cctrl

