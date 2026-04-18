from rest_framework import permissions


class EitherIsAdminThenAllowAnyOrIsOwnerThenAllowSafe(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user

        return False # разве это не избыточная строка?