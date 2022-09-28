from django.shortcuts import render
from .models import UserProfile
###########################################
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
###########################################
from .serializers import UserProfileSerializer
from .permissions import UpdateSelfProfile

# Create your views here.


class UserProfileViewSet(ModelViewSet):
    #add endpoint to handle user profile requests

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    # Give the ViewSet the permission class and the auth class
    # Each token gets to compare permissions and either pass or fail
    authentication_classes = (TokenAuthentication,) #tuple
    permission_classes = (UpdateSelfProfile,) #tuple

    #add a search functionality by name or email
    filter_backends = (filters.SearchFilter,) #tuple
    search_fields = ('name', 'email',) #tuple
    
##############################################################
##############################################################        
##############################################################

class UserLoginApiView(ObtainAuthToken):
    #add user login api endpoint
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

##############################################################
##############################################################        
##############################################################
