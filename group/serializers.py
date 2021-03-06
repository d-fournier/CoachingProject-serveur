from rest_framework import serializers
from .models import Group
from user.serializers import UserProfileReadSerializer
from sport.serializers import SportSerializer

class GroupReadSerializer(serializers.ModelSerializer):
	sport = SportSerializer(read_only=True)
	
	class Meta:
		model = Group
		fields = ('__all__')

class GroupCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('id','name','description','sport','city','private')