import inspect
import warnings
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth.backends import UserModel
from django.conf import settings
import requests


class TroodAuth(RemoteUserBackend):

    @staticmethod
    def has_module_perms(user, app):
        return True

    def get_token(self, request):
        token = request.META.get('Authorization')
        if token is None:
            token = request.headers.get('Authorization')

        return token

    def verify_token(self, headers):
        response = requests.post(f'{settings.AUTH_URL}api/v1.0/verify-token/', headers=headers)
        if response.status_code != 200:
            return None
        return response.json()['data']

    def try_login(self, data):
        login_data = {
            'login': data.get('username'),
            'password': data.get('password')
        }
        response = requests.post(f'{settings.AUTH_URL}api/v1.0/login/', json=login_data)
        if response.status_code != 200:
            return None
        return response.json()['data']

    def get_user(self, username):
        if not isinstance(username, int):
            user, created = UserModel._default_manager.get_or_create(**{
                UserModel.USERNAME_FIELD: username
            })
            if not user.is_superuser:
                user.is_superuser = True
                user.is_staff = True
                user.save()

            return user

    def authenticate(self, request, remote_user=None):
        token = self.get_token(request)
        if token:
            headers = {'Authorization': token}
            user = self.verify_token(headers)
        else:
            user = self.try_login(request.POST)

        if not user:
            return None
        return self.get_user(user['login'])
