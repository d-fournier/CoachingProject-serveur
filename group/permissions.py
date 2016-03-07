from rest_framework import permissions
from .models import Group
from .serializers import GroupReadSerializer
from user.models import UserProfile

class GroupPermission(permissions.BasePermission):
	
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
		# Check permissions for read-only request
			return True
		else:
			# Check permissions for write request
			if request.user.is_superuser:
				return True
			elif request.user.is_authenticated():
				if request.method=='POST':
					return True
				else:
					return False
			else:
				return False

	def has_object_permission(self, request, view, obj):
		if request.user.is_authenticated():
			up = UserProfile.objects.get(user=request.user)
			return request.user.is_superuser or (up in obj.members.all())
		else:
			return False