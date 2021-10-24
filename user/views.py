from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.http import JsonResponse
from .models import Module,Submodule,Resource
from rest_framework.views import APIView


from user.serializers import UserSerializer, AuthTokenSerializer,ModuleSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
class IndexViews(APIView):
    def get(self,request):
        recent_posts=Module.objects.all().order_by('-created_at')
        serializer=ModuleSerializer(recent_posts)
        return JsonResponse({
        'recentpost_list':serializer.data
        })

class NewModuleViews(APIView):
    res=""
    def post(self,request):
        serializer_class=ModuleSerializer
        data=request.data
        
        title = data["title"]
        print(title)
        description=data['description']
        serializer=ModuleSerializer(data=data)
        #user = user.objects.get(id=request.session.get('user_id'))
        if serializer.is_valid():
            new_post = Module.objects.create(title=title,description=description)
            new_post.save()
            res="success"
        else:
            res="error"
        return JsonResponse({"status":res})

