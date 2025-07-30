from enum import StrEnum


class UserRole(StrEnum):
    OWNER = "owner"
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


userrole = "admin"
user = UserRole('user')
print(user.value, user.name, user)