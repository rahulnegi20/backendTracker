from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.http import JsonResponse

from user.serializers import UserSerializer, AuthTokenSerializer

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

def new_post(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            description=request.POST.get('description')
            #user = user.objects.get(id=request.session.get('user_id'))
            new_post = Post(title=title,description=description)
            new_post.save()
            res="success"
        except ValueError:
            res="error"
            
    return JsonResponse({"result":res})
