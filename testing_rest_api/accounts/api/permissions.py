from rest_framework import permissions

class AnonUserPermissionOnly(permissions.BasePermission):
    """
    Global permission check for Anonymous Users.
    """

    message = 'Already authenticated'
    def has_permission(self, request, view):
        return not request.user.is_authenticated



# class BlacklistPermission(permissions.BasePermission):
#     """
#     Global permission check for blacklisted IPs.
#     """
#
#     def has_permission(self, request, view):
#         ip_addr = request.META['REMOTE_ADDR']
#         blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
#         return not blacklisted


