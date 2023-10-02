from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter


# подключите UserViewSet из Djoser.views к нашим urls.py
# для этого рекомендуется использовать SimpleRouter
users_router = SimpleRouter()

# обратите внимание, что здесь в роутер мы регистрируем ViewSet,
# который импортирован из приложения Djoser
users_router.register("", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
]


# =========================================================================
# from django.urls import path
#
# from users import views
#
# urlpatterns = [
#     path("signup", views.SignupView.as_view(), name='signup'),
#     path("login", views.LoginView.as_view(), name='login'),
#     path("profile", views.ProfileView.as_view(), name='profile'),
#     path("update_password", views.UpdatePasswordView.as_view(), name='update_password'),
# ]
