from django.urls import path
from .views import UserRegistrationAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from .import views
from .views import UserRegistrationAPIView

urlpatterns = [
    path('register/',UserRegistrationAPIView.as_view()),
    # path('login/', ObtainAuthToken.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
     
]
