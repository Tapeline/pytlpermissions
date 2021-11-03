def hasPermission(perms, perm):
    if "*" in perms: return True
    splitted_perm = perm.split(".")
    concat_perm = ""
    for pos, i in enumerate(splitted_perm):
        concat_perm += f"{i}." if pos + 1 != len(splitted_perm) else i
        if concat_perm + "*" in perms: return True
    return False
