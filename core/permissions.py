import requests
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

class TroodAuth(IsAuthenticated):

    def has_permission(self, request, view):
        # XXX: Don't use in production
        is_test_token = request.META.get('Authorization') == 'Token TEST_TOKEN'
        if is_test_token:
            return True

        url = f'{settings.AUTH_URL}api/v1.0/verify-token/'
        headers = {'Authorization': self.get_token(request)}
        response = requests.post(url, headers=headers)
        if response.status_code != 200:
            return False

        return response.json()['status'] == 'OK'

    def get_token(self, request):
        token = request.META.get('Authorization')
        if token is None:
            token = request.headers.get('Authorization')

        return token
