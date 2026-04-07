def check_permissions(user):
    if not user:
        return "[AUTH] Permission denied"
    return "[AUTH] Operator verified"