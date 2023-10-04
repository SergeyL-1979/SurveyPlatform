from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

from djoser.conf import settings
from djoser.serializers import TokenCreateSerializer


User = get_user_model()
# Здесь нам придется переопределить сериалайзер, который использует djoser
# для создания пользователя из-за того, что у нас имеются нестандартные поля


class CustomTokenCreateSerializer(TokenCreateSerializer):

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user:  # and self.user.is_active:
            return attrs
        self.fail("invalid_credentials")


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
