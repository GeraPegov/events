
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .serializers import RegisterSerializer, LoginSerializer, RefreshTokenSerializer
from .models import AuthorizationModel
from django.views.generic import TemplateView
from jwt_auth.forms import AuthorizationForm, RefreshTokenForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse
import time

class RegisterTemplatesView(TemplateView, APIView):
    template_name = 'auth/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorizationForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            serializer = RegisterSerializer(data=form.cleaned_data)
        if serializer.is_valid():
            user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=status.HTTP_201_CREATED)

class LoginTemplatesView(TemplateView, APIView):
    template_name = 'auth/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorizationForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = AuthorizationForm(request.POST)
        print(form.is_valid(), 'qwerqwerqwer')
        if not form.is_valid():
            return Response({'error': 'not validated'})
        else:
            form.is_valid()
        serializer = LoginSerializer(data=form.cleaned_data)
        if not serializer.is_valid():
            return Response({'error': 'not validated'})
        else:
            serializer.is_valid()

        user = AuthorizationModel.objects.get(login=serializer.validated_data['login'])
        if not check_password(serializer.validated_data['password'], user.password):
            return Response(
                {"error": "Invalid password"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        refresh = RefreshToken.for_user(user)
        return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=status.HTTP_201_CREATED)

class RefreshTokenAPIView(APIView):
    def post(self, request):
        serializer = RefreshTokenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            refresh = RefreshToken(serializer.validated_data['refresh_token'])
            return Response({
                "access": str(refresh.access_token)
            })
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_401_UNAUTHORIZED
            )

