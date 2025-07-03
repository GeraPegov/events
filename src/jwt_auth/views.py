
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .models import AuthorizationModel
from django.contrib.auth.hashers import make_password



class RegisterTemplatesView(APIView):
    def post(self, request, *args, **kwargs):
        new_login = request.data['login']
        new_password = make_password(request.data['password'])
        id_user = AuthorizationModel.objects.create(
            login=new_login,
            password=new_password
        )
        refresh = RefreshToken.for_user(id_user)
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        })

class LoginTemplatesView(APIView):
    def post(self, request, *args, **kwargs):
        new_login = request.data['login']
        new_password = request.data['password']
        id_user = AuthorizationModel.objects.filter(
            login=new_login,
        )
        if not check_password(new_password, id_user.password):
            return Response({
                'error': 'not password'
            })
        refresh = RefreshToken.for_user(id_user)
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        })

class RefreshTokenAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.body)