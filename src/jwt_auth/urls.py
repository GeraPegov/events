from django.urls import path
from .views import RegisterTemplatesView, LoginAPIView, RefreshTokenAPIView,  LoginView

urlpatterns = [
    path('api/auth/register/', RegisterTemplatesView.as_view(), name='register-api'),
    path('api/auth/login/', LoginAPIView.as_view(), name='login-api'),
    path('api/auth/refresh/', RefreshTokenAPIView.as_view(), name='refresh-api'),
    # path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]