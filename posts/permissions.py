from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user.profile.is_sender)
        return bool(
            request.method in SAFE_METHODS or
            request.user.profile.is_sender
        )

class IsNotAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user.profile.is_sender)
        return bool(
            request.method in SAFE_METHODS
        )

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.profile.id == request.user.profile.id

