from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import Q


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()

class AuthView(APIView):
    permission_classes = [permissions.AllowAny]  #Important to include

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            username = request.data.get('username', None)
            password = request.data.get('password')
            email = request.data.get('email', None)
            qs = User.objects.filter(
                Q(username__iexact=username) | Q(email__iexact=email))
            print(qs)
            print(qs.count())
            if qs.count() == 1:
                user_obj = qs.first()
                if user_obj.check_password(password):
                    user = user_obj
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)
                    response = jwt_response_payload_handler(token, user, request)
                    return Response(response)
                else:
                    return Response({'detail': 'Incorrect Password'}, status=400)
            else:
                return Response({'detail': 'Authentication resulting in multiple users'}, status=400)
        else:
            return Response({'detail': 'Already signed in'}, status=400)