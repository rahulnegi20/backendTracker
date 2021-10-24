from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('createmodule/',views.NewModuleViews.as_view(),name='module'),
    path('getrecentlist/',views.IndexViews.as_view(),name='latest_view')

]