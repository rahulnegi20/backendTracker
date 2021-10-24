from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('create-module/', views.ModuleCreateView.as_view(), name="create-module"),
    path('list-module/', views.ModuleListView.as_view(), name="module-list"),
    path('<int:apk>/create-submodule/', views.SubModuleCreateView.as_view(), name="create-module"),
    path('<int:apk>/list-submodule/', views.SubModuleListView.as_view(), name="submodule-list"),
]