from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.conf import settings
from django.utils import timezone

expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expires': timezone.now() + expire_delta
        # 'user': UserSerializer(user, context={'request': request}).data
    }

class AuthView(APIView):
    permission_classes = [permissions.AllowAny]  #Import to include

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(password=password, username=username)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = jwt_response_payload_handler(token, user, request)
        return Response(response)



