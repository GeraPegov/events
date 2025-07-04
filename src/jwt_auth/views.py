from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import AuthorizationModel


class RegisterTemplatesView(APIView):
    def post(self, request, *args, **kwargs):
        new_login = request.data['login']
        new_password = make_password(request.data['password'])
        id_user = AuthorizationModel.objects.create(
            login=new_login,
            password=new_password
        )
        refresh = RefreshToken.for_user(id_user)
        response = JsonResponse({
            'access token': str(refresh.access_token),
            'refresh token': str(refresh)
        })

        response.set_cookie(
            'access_token',
            str(refresh.access_token),
            httponly=True,
            samesite='Lax'
        )
        response.set_cookie(
            'refresh_token',
            str(refresh),
            httponly=True,
            samesite='Lax'
        )

        return response


class LoginTemplatesView(APIView):
    def post(self, request, *args, **kwargs):
        new_login = request.data['login']
        new_password = request.data['password']
        id_user = AuthorizationModel.objects.filter(
            login=new_login,
        ).first()
        if not check_password(new_password, id_user.password):
            return Response({
                'error': 'not password'
            })
        refresh = RefreshToken.for_user(id_user)

        response = JsonResponse({
            'access token': str(refresh.access_token),
            'refresh token': str(refresh)
        })
        response.set_cookie(
            'access_token',
            str(refresh.access_token),
            httponly=True,
            samesite='Lax'
        )
        response.set_cookie(
            'refresh_token',
            str(refresh),
            httponly=True,
            samesite='Lax'
        )

        return response


class RefreshTokenAPIView(APIView):
    def post(self, request, *args, **kwargs):
        old_token = request.COOKIES.get('refresh_token')
        new_token = RefreshToken(old_token)
        response = JsonResponse({
            'access_tokens': str(new_token.access_token)
        })
        response.set_cookie(
            'access_token',
            str(new_token),
            httponly=True,
            samesite='Lax'
        )
        return response
