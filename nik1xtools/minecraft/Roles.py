import json
from nik1xtools.default.FileManager import File


class RoleManager:

    def __init__(self, config_file: str, users_file: str):
        self.config_file = File(config_file, create_if_not_exists=True)
        self.users_file = File(users_file, create_if_not_exists=True)

    # addRole(
    #   role_name - Str | ex. User[role] = role_name,
    #   role_title - Str | ex. Your role is {role_title}
    #   accessed_commands - List | ex. ["/ban", "/op"]
    # )
    def addRole(self, role_name: str, role_title: str, accessed_commands: list) -> bool:
        RolesList = json.loads(self.config_file.read())
        if role_name not in RolesList.keys():
            RolesList[role_name] = {
                "title": role_title,
                "access_to": accessed_commands
            }
            self.config_file.write(
                json.dumps(RolesList, indent=4, sort_keys=True)
            )
            return True
        return False

    # getRole(
    #   role_name - Str
    # )
    def getRole(self, role_name: str) -> dict or bool:
        RolesList = json.loads(self.config_file.read())
        if role_name in RolesList:
            return RolesList[role_name]
        else:
            return False

    # removeRole(
    #   role_name - Str
    # )
    def removeRole(self, role_name) -> bool:
        RolesList = json.loads(self.config_file.read())
        UsersList = json.loads(self.users_file.read())
        if role_name in RolesList.keys():
            for user in UsersList:
                if UsersList[user] == role_name:
                    UsersList.pop(user)
                    self.users_file.write(json.dumps(UsersList, indent=4, sort_keys=True))
            RolesList.pop(role_name)
            self.config_file.write(json.dumps(RolesList, indent=4, sort_keys=True))
            return True
        return False

    # editRole(
    #   role_name - Str
    #   role_new_name - Set None, if not need to change, else = role key will be changed
    #   role_title - Str | ex. Your role is {role_title}
    #   accessed_commands - List | ex. ["/ban", "/op"]
    # )
    def editRole(self, role_name, role_new_name: str = None, role_title: str = None, accessed_commands: list = None) -> bool:
        RolesList = json.loads(self.config_file.read())
        UsersList = json.loads(self.users_file.read())
        if role_name in RolesList.keys():
            # Update role name
            if role_new_name not in RolesList.keys():
                RolesList[role_new_name] = RolesList[role_name]
                self.removeRole(role_name)
                for user in UsersList:
                    if UsersList[user] == role_name:
                        UsersList[user] = role_new_name
                        self.users_file.write(json.dumps(UsersList, indent=4, sort_keys=True))
                role_name = role_new_name
            else:
                return False
            # Update role title
            if role_title is not None:
                RolesList[role_name]["title"] = role_title
            # Update role access_to
            if accessed_commands is not None:
                RolesList[role_name]["access_to"] = accessed_commands

            self.config_file.write(json.dumps(RolesList, indent=4, sort_keys=True))
            return True
        return False

    # userSetRole(
    #   user_id - int | ex. 1
    #   role_name - str | ex. admin
    # )
    def userSetRole(self, user_id: int, role_name: str) -> bool:
        UsersData = json.loads(self.users_file.read())
        RolesList = json.loads(self.config_file.read())
        if role_name in RolesList.keys():
            UsersData[str(user_id)] = role_name
            self.users_file.write(json.dumps(UsersData, indent=4, sort_keys=True))
            return True
        return False

    # userRemoveRole(
    #   user_id - int | ex. 1
    # )
    def userRemoveRole(self, user_id: int) -> bool:
        UsersData = json.loads(self.users_file.read())
        if str(user_id) in UsersData.keys():
            UsersData.pop(str(user_id))
            self.users_file.write(json.dumps(UsersData, indent=4, sort_keys=True))
            return True
        return False

    # userGet(
    #   user_id - int | ex. 1
    # )
    def userGet(self, user_id: int) -> bool or str:
        UsersData = json.loads(self.users_file.read())
        if str(user_id) in UsersData.keys():
            return UsersData[str(user_id)]
        return False