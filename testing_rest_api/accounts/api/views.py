from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework.response import Response
from django.db.models import Q
from .serializers import UserSerializer


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


# class RegisterView2(APIView):
#     permission_classes = [permissions.AllowAny]  #Important to include
#
#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             username = request.data.get('username', None)
#             password = request.data.get('password')
#             password2 = request.data.get('password2')
#             email = request.data.get('email', None)
#             qs = User.objects.filter(
#                 Q(username__iexact=username) | Q(email__iexact=email))
#             if qs.exists():
#                 return Response({'detail': 'User already exists'}, status=400)
#             if password != password2:
#                 return Response({'detail': 'Passwords do not match'}, status=400)
#             user = User.objects.create(username=username or email, email=email)
#             user.set_password(password)
#             user.save()
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             response = jwt_response_payload_handler(token, user, request)
#             return Response(response)
#         else:
#             return Response({'detail': 'Already signed in'}, status=400)


class RegisterView(generics.CreateAPIView):
    # Same as RegisterView2 but moved most methods to serializerclass
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self, *args, **kwargs):
        #makes sure the request is passed to the rerializer so it can be used in token response"
        return super(RegisterView, self).get_serializer_context(*args, **kwargs)

