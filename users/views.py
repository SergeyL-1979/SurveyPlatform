from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class UserActivationView(APIView):

    def get(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/users/activate/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        content = result.text
        return Response(content)



# from django.contrib.auth import login, logout
# from rest_framework import permissions
# from rest_framework.generics import (
#     CreateAPIView,
#     GenericAPIView,
#     RetrieveUpdateDestroyAPIView,
#     UpdateAPIView,
# )
# from rest_framework.response import Response
#
# from users.models import User
# from users.serializers import (
#     CreateUserSerializer,
#     LoginSerializer,
#     UserSerializer,
#     UpdatePasswordSerializer,
# )
#
#
# class SignupView(CreateAPIView):
#     """ Вход для пользователя """
#     model = User
#     permission_classes = [permissions.AllowAny]
#     serializer_class = CreateUserSerializer
#
#     def perform_create(self, serializer):
#         super().perform_create(serializer)
#         login(
#             self.request,
#             user=serializer.user,
#             backend="django.contrib.auth.backends.ModelBackend",
#         )
#
#
# class LoginView(GenericAPIView):
#     """ Авторизация пользователя """
#     serializer_class = LoginSerializer
#
#     def post(self, request, *args, **kwargs):
#         s: LoginSerializer = self.get_serializer(data=request.data)
#         s.is_valid(raise_exception=True)
#         user = s.validated_data["user"]
#         login(request, user=user)
#         user_serializer = UserSerializer(instance=user)
#         return Response(user_serializer.data)
#
#
# class ProfileView(RetrieveUpdateDestroyAPIView):
#     """ Профиль пользователя """
#     model = User
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UserSerializer
#
#     def get_object(self):
#         return self.request.user
#
#     def delete(self, request, *args, **kwargs):
#         logout(request)
#         return Response({})
#
#
# class UpdatePasswordView(UpdateAPIView):
#     """ Редактирование пароля """
#     model = User
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UpdatePasswordSerializer
#
#     def get_object(self):
#         return self.request.user