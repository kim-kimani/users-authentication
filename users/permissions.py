from rest_framework import permissions

class IsUserOwnerGetAndPostOnly(permissions.BasePermission):
    """
    Custom permission for UserViewSet to only allow owners of an object to edit it.
    Allows GET and POST requests for all users.
    """
    
    def has_permission(self, request, view):
        return True  # Allow all users to make GET and POST requests
    
    def has_object_permission(self, request, view, obj):
        # Allow owners of the object to edit it
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user == obj
        
        return False

    