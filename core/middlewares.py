from django.core.exceptions import ImproperlyConfigured
from django.contrib import auth
from django.contrib.auth.middleware import RemoteUserMiddleware

class TroodAuth(RemoteUserMiddleware):
    header = "Authorization"
    force_logout_if_no_header = False

    def process_request(self, request):
        user = auth.authenticate(request)
        if user:
            request.user = user
            auth.login(request, user)
