# 
# TODO check if this class is right


class User ():
    # private:
    """
    id # int
    username # string
    fortschritts_lvl # float
    invite_link # string
    atk_link # string
    arbeiter_gesamt # int
    truppen_gesamt #int
    last_message_timestamp # time
    inactive # bool
    id_clan_membership # int
    id_hierarchy_lvl # int
    ids_user_role # array
    """
    def __init__(self, **kwargs):
        """
         @**kwargs:
          id: int
          username: string
          fortschritts_lvl # float
          invite_link # string
          atk_link # string
          arbeiter_gesamt # int
          truppen_gesamt #int
          last_message_timestamp # time
          inactive # bool
          id_clan_membership # int
          id_hierarchy_lvl: int
          ids_user_role: array = []
        """
        missing = "User __init__: Missing "
        if "id" in kwargs.keys():
            self.id = int(kwargs["id"])
        else:
            raise ValueError(missing+"id")
        if "username" in kwargs.keys():
            self.username = str(kwargs["username"])
        else:
            raise ValueError(missing+"username")
        if "fortschritts_lvl" in kwargs.keys():
            self.fortschritts_lvl = int(kwargs["fortschritts_lvl"])
        if "invite_link" in kwargs.keys():
            self.invite_link = int(kwargs["invite_link"])
        if "atk_link" in kwargs.keys():
            self.atk_link = int(kwargs["atk_link"])
        if "arbeiter_gesamt" in kwargs.keys():
            self.arbeiter_gesamt = int(kwargs["arbeiter_gesamt"])
        if "truppen_gesamt" in kwargs.keys():
            self.truppen_gesamt = int(kwargs["truppen_gesamt"])
        if "last_message_timestamp" in kwargs.keys():
            self.last_message_timestamp = int(kwargs["last_message_timestamp"])
        if "inactive" in kwargs.keys():
            self.inactive = int(kwargs["inactive"])
        if "id_clan_membership" in kwargs.keys():
            self.id_clan_membership = int(kwargs["id_clan_membership"])
        if "id_hierarchy_lvl" in kwargs.keys():
            self.id_hierarchy_lvl = int(kwargs["id_hierarchy_lvl"])
        else:
            raise ValueError(missing+"id_hierarchy_lvl")
        if "ids_user_role" in kwargs.keys():
            self.ids_user_role = list(kwargs["ids_user_role"])
        else:
            self.ids_user_role = []

    # public:
    def getId(self):
        return self.id

    def getUsername(self):
        return self.username

    def setUsername(self, new_username):
        self.username = str(new_username)

    def getFortschrittsLvl(self):
        return self.fortschritts_lvl

    def setFortschrittsLvl(self, fortschritts_lvl):
        self.fortschritts_lvl = fortschritts_lvl

    def getInviteLink(self):
        return self.invite_link

    def setInviteLink(self, invite_link):
        self.invite_link = invite_link

    def getAtkLink(self):
        return self.atk_link

    def setAtkLink(self, atk_link):
        self.atk_link = atk_link

    def getArbeiterGesamt(self):
        return self.arbeiter_gesamt

    def setArbeiterGesamt(self, arbeiter_gesamt):
        self.arbeiter_gesamt = arbeiter_gesamt

    def getTruppenGesamt(self):
        return self.truppen_gesamt

    def setTruppenGesamt(self, truppen_gesamt):
        self.truppen_gesamt = truppen_gesamt

    def getLastMessageTimestamp(self):
        return self.last_message_timestamp

    def setLastMessageTimestamp(self, last_message_timestamp):
        self.last_message_timestamp = last_message_timestamp

    def getInactive(self):
        return self.inactive

    def setInactive(self, inactive):
        self.inactive = inactive

    def getIdClanMembership(self):
        return self.id_clan_membership

    def setIdClanMembership(self, id_clan_membership):
        self.id_clan_membership = id_clan_membership

    def getIdHierarchyLvl(self):
        return self.id_hierarchy_lvl

    def setIdHierarchyLvl(self, id_hierarchy_lvl):
        self.id_hierarchy_lvl = id_hierarchy_lvl

    """
    hierarchy lvl and permission stuff
    """
    def getHierarchyLvl(self): 
        return self.id_hierarchy_lvl

    def upgrade(self): 
        self.id_hierarchy_lvl -= 1
        return True

    def downgrade(self): 
        self.id_hierarchy_lvl += 1
        return True

    def getUserRoles(self): 
        return self.ids_user_role

    def addUserRole(self, id_user_role): 
        if int(id_user_role) in self.ids_user_role:
                return False
        else:
                self.ids_user_role.append(int(id_user_role))
                return True

    def removeUserRole(self, id_user_role): 
        if int(id_user_role) in self.ids_user_role:
                self.ids_user_role.remove(int(id_user_role))
                return True
        else:
                return False
