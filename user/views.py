from django.db.models.query import QuerySet
from rest_framework import generics, status, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import UserSerializer, AuthTokenSerializer, ModuleCreateSerializer, SubModuleCreateSerializer \
                            , ResourceCreateSerializer
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


class SubModuleCreateView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SubModuleCreateSerializer
    lookup_url_kwarg = 'apk'
    http_method_names = ['post']

    def post(self, request, apk, *args, **kwargs):
        module = models.Module.objects.get(pk=apk)
        print('THIS IS THE MOUDLE',module)
        title = request.data['title']
        description = request.data['description']

        instance = models.Submodule.objects.create(module=module, title=title, description=description)
        if instance is not None:
            instance.save()
            return Response(status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST) 

class SubModuleListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_url_kwarg = 'apk'
    lookup_field = 'apk'

    def get(self,request, apk, format=None):
        print('THIS IS APK',apk)
        queryset = models.Submodule.objects.filter(module_id=apk)
        print('WUEAKSASD MSAKD  SD K KSA', queryset)
        serializer = ModuleCreateSerializer(queryset, many=True)
        return Response(serializer.data)


class ResourceCreateView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class =  ResourceCreateSerializer
    lookup_url_kwarg = 'bpk'
    lookup_field = 'bpk'
    http_method_names = ['post']

    def post(self, request, bpk, *args, **kwargs):
        submodule = models.Submodule.objects.get(pk=bpk)
        print('THIS IS THE res',submodule)
        title = request.data['title']
        url = request.data['url']

        instance = models.Resource.objects.create(submodule=submodule, title=title, url=url)
        if instance is not None:
            instance.save()
            return Response(status.HTTP_200_OK)


class ResourceListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_url_kwarg = 'bpk'
    lookup_field = 'bpk'

    def get(self, request, apk, bpk, format=None):
        print('THIS IS APK', bpk)
        queryset = models.Resource.objects.filter(submodule_id=bpk)
        print('WUEAKSASD MSAKD  SD K KSA', queryset)
        serializer =  ResourceCreateSerializer(queryset, many=True)
        return Response(serializer.data)
