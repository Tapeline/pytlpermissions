# pytlpermissions

Simple function to check whether or not user has permission.

# Usage

`hasPermission(list, permission)` - checks if `permission` in permissions `list`. Supports `*` notation. E.g.: `["*"]`,`roles.*` > `true`, `["admin.ban.*"]`,`admin.ban.user.Hacker` > `true`


Example:
```
import permissions

perms = ["admin.*", "roles.create.user.*"]
print(permissions.hasPermission(perms, "*"))
print(permissions.hasPermission(perms, "roles.delete.Tapeline"))
print(permissions.hasPermission(perms, "admin.ban.*"))
print(permissions.hasPermission(perms, "roles.create.user.Tapeline"))
```
Console output:
```
False
False
True
True
```
