from .Roles import RoleManager

class CommandManager:

    def __init__(self, manager: RoleManager):
        self.manager = manager

    def canUse(self, user_id: int, command: str) -> bool:
        user_role = self.manager.userGet(user_id)
        role = self.manager.getRole(user_role)
        access_to = role["access_to"]

        cmd_prefix = ""
        if " " in command:
            zero_ = command.split(" ")[0]
            if command.split(" ")[0].startswith("/"):
                cmd_prefix = zero_
            else:
                cmd_prefix = "/"+zero_
        else:
            if command.split(" ")[0].startswith("/"):
                cmd_prefix = command
            else:
                cmd_prefix = "/"+command

        if cmd_prefix in access_to:
            return True
        else:
            return False