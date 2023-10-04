from django.urls import include, path
from users.dj_views import UserViewSet
from rest_framework.routers import SimpleRouter

from users import views

# подключите UserViewSet из Djoser.views к нашим urls.py
# для этого рекомендуется использовать SimpleRouter
users_router = SimpleRouter()

# обратите внимание, что здесь в роутер мы регистрируем ViewSet,
# который импортирован из приложения Djoser
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),

    path('users/activate/<uid>/<token>', views.UserActivationView.as_view()),

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
