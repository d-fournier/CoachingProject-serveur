from django.shortcuts import render
from .serializers import SportSerializer
from .models import Sport
from rest_framework import viewsets, permissions
from rest_framework.decorators import detail_route

# Create your views here.
class SportViewSet(viewsets.ModelViewSet):
	queryset = Sport.objects.all()
	serializer_class = SportSerializer
	permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]