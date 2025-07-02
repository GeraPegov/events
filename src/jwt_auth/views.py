
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


# class RegisterView(TemplateView):
#     template_name = 'auth/register.html'  


class LoginView(TemplateView):
    template_name = 'auth/login.html'


# class RegisterAPIView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 "access": str(refresh.access_token),
#                 "refresh": str(refresh)
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterTemplatesView(TemplateView):
    template_name = 'auth/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorizationForm()
        return context
    
    def post(self, request):
        print('hellllo')
        form = AuthorizationForm(request.POST)
        print(form, 'hellllo')
        if form.is_valid():
            serializer = RegisterSerializer(form)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken(serializer)
        return HttpResponse({
            'access_token': refresh,
            "refresh_token": refresh.access_token
        })

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = AuthorizationModel.objects.get(login=serializer.validated_data['login'])
            if not check_password(serializer.validated_data['password'], user.password):
                return Response(
                    {"error": "Invalid password"}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })
            
        except AuthorizationModel.DoesNotExist:
            return Response(
                {"error": "User not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

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

