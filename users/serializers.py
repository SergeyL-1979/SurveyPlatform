from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models import User


# User = get_user_model()
# Здесь нам придется переопределить сериалайзер, который использует djoser
# для создания пользователя из-за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    # role = serializers.SlugRelatedField(slug_field='user', read_only=True)
    """ Убедитесь, что пароль содержит не менее 8 символов, не более 128,
    и так же что он не может быть прочитан клиентской стороной """
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    ''' Клиентская сторона не должна иметь возможность отправлять токен вместе с
    запросом на регистрацию. Сделаем его доступным только на чтение. '''
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta(BaseUserRegistrationSerializer.Meta):
        """ Перечислить все поля, которые могут быть включены в запрос
        или ответ, включая поля, явно указанные выше. """
        model = User
        fields = ['email', 'first_name', 'last_name', 'token', 'password']

    def create(self, validated_data):
        """ Использовать метод create_user, который мы
        написали ранее, для создания нового пользователя. """
        return User.objects.create_user(**validated_data)


class CurrentUserSerializer(serializers.ModelSerializer):
    """ Убедитесь, что пароль содержит не менее 8 символов, не более 128,
    и так же что он не может быть прочитан клиентской стороной """
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    """ Клиентская сторона не должна иметь возможность отправлять токен вместе с
    запросом на регистрацию. Сделаем его доступным только на чтение. """
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta(BaseUserRegistrationSerializer.Meta):
        """ Перечислить все поля, которые могут быть включены в запрос
        или ответ, включая поля, явно указанные выше. """
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'token', 'last_login', ]

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get("email", instance.email)
    #     instance.first_name = validated_data.get("first_name", instance.first_name)
    #     instance.last_name = validated_data.get("last_name", instance.last_name)
    #     instance.phone = validated_data.get("phone", instance.phone)
    #     instance.last_login = validated_data.get("last_login", instance.last_login)
    #     instance.image = validated_data.get("image", instance.image)
    #     instance.save()
    #     return instance


# ======================================================================
# from django.contrib.auth import authenticate
# from django.contrib.auth.password_validation import validate_password
# from rest_framework import serializers
# from rest_framework.exceptions import ValidationError

# from users.models import User
# ======================================================================
# ======================================================================
# class CreateUserSerializer(serializers.ModelSerializer):
#     """ Создаем пользователя и регистрируем его. """
#     password = serializers.CharField(write_only=True, validators=[validate_password])
#     password_repeat = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         read_only_fields = ("id",)
#         fields = [
#             "id",
#             "username",
#             "first_name",
#             "last_name",
#             "email",
#             "password",
#             "password_repeat",
#         ]
#
#     def validate(self, attrs: dict):
#         password: str = attrs.get("password")
#         password_repeat: str = attrs.pop("password_repeat", None)
#         if password != password_repeat:
#             raise ValidationError("password and password_repeat is not equal")
#         return attrs
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         self.user = user
#         return user
#
#
# class LoginSerializer(serializers.Serializer):
#     """ Авторизация пользователя на сайте """
#     username = serializers.CharField(write_only=True)
#     password = serializers.CharField(write_only=True)
#
#     def validate(self, attrs: dict):
#         username = attrs.get("username")
#         password = attrs.get("password")
#         user = authenticate(username=username, password=password)
#         if not user:
#             raise ValidationError("username or password is incorrect")
#         attrs["user"] = user
#         return attrs
#
#
# class UserSerializer(serializers.ModelSerializer):
#     """ Вывод объекта пользователя """
#     class Meta:
#         model = User
#         read_only_fields = ("id",)
#         fields = [
#             # "id",
#             "username",
#             "first_name",
#             "last_name",
#             "email",
#         ]
#
#
# class UpdatePasswordSerializer(serializers.ModelSerializer):
#     """ Модель редактирования пароля """
#     old_password = serializers.CharField(write_only=True)
#     new_password = serializers.CharField(write_only=True, validators=[validate_password])
#
#     class Meta:
#         model = User
#         read_only_fields = ("id",)
#         fields = ("old_password", "new_password")
#
#     def validate(self, attrs):
#         old_password = attrs.get("old_password")
#         user: User = self.instance
#         if not user.check_password(old_password):
#             raise ValidationError({"old_password": "field is incorrect"})
#         return attrs
#
#     def update(self, instance: User, validated_data):
#         instance.set_password(validated_data["new_password"])
#         instance.save(update_fields=["password"])
#         return instance
