from django.db.models.query import QuerySet
from rest_framework import generics, status, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import UserSerializer, AuthTokenSerializer, ModuleCreateSerializer
from . import models


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_name': user.name,
            'email': user.email
        })

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class ModuleCreateView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ModuleCreateSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user = self.request.user
        print('Hello i am user', user)
        title = request.data['title']
        description = request.data['description']

        instance = models.Module.objects.create(created_by=user, title=title, description=description)
        if instance is not None:
            instance.save()
            return Response(status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST) 

class ModuleListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


    def get(self, request, format=None):
        queryset = models.Module.objects.all()
        serializer = ModuleCreateSerializer(queryset, many=True)
        return Response(serializer.data)

# class SubModuleCreateView(APIView):
#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = SubModuleCreateSerializer
#     http_method_names = ['post']

#     def post(self, request, *args, **kwargs):
#         user = self.request.user
#         title = request.data['title']
#         description = request.data['description']

#         instance = models.Module.objects.create(created_by=user, title=title, description=description)
#         if instance is not None:
#             instance.save()
#             return Response(status.HTTP_200_OK)

#         return Response(status.HTTP_400_BAD_REQUEST) 