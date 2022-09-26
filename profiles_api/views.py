from django.shortcuts import render
from .models import UserProfile
from rest_framework.viewsets import ModelViewSet
from .serializers import UserProfileSerializer
# Create your views here.


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()