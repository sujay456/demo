
from rest_framework import permissions

class IsAdminorReadonly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method == 'GET'


class ReviewUserorReadonly(permissions.BasePermission):
    # message="Hello from server"
    def has_object_permission(self, request, view,obj):
        
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            return obj.review_user==request.user
            # Check permissions for write request