from django.http import HttpResponseRedirect
from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in ['/api/auth/login/', '/api/auth/register/']:
            return self.get_response(request)

        if request.path.startswith('/events/'):
            token = request.COOKIES.get('access_token')
            if not token:
                return HttpResponseRedirect('/api/auth/login/')

            try:
                JWTAuthentication().authenticate(request)
            except Exception:
                return HttpResponseRedirect('/login')

        return self.get_response(request)
