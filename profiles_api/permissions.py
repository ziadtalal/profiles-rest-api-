from rest_framework import permissions


class UpdateOwnProfiles(permissions.BasePermission):
    """Allow users edit there own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit there own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users update there own status"""
    def has_object_permission(self, request, view, obj):
        """check user is trying to update there own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
