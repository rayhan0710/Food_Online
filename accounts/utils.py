


def detectUser(user):
    if user.role == 1:
        rediractUrl = 'vendorDashboard'
        return rediractUrl
    elif user.role == 2:
        rediractUrl = 'custDashboard'
        return rediractUrl
    elif user.role == None and user.is_superadmin:
        rediractUrl = '/admin'
        return rediractUrl