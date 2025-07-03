from django.urls import path
from .views import RegisterTemplatesView, LoginTemplatesView, RefreshTokenAPIView

urlpatterns = [
    path('api/auth/register/', RegisterTemplatesView.as_view(), name='register-api'),
    path('api/auth/login/', LoginTemplatesView.as_view(), name='login-api'),
    path('api/auth/refresh/', RefreshTokenAPIView.as_view(), name='refresh-api'),
]