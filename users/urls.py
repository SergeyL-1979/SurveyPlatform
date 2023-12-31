from django.urls import include, path
# from users.dj_views import UserViewSet
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

# from users import views

# подключите UserViewSet из Djoser.views к нашим urls.py
# для этого рекомендуется использовать SimpleRouter
users_router = SimpleRouter()

# обратите внимание, что здесь в роутер мы регистрируем ViewSet,
# который импортирован из приложения Djoser
users_router.register("", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
]

