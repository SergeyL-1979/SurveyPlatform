from django.contrib import admin

from users.models import User


# Aдминка для пользователя - как реализовать ее можно подсмотреть в документацию django
# Обычно её всегда оформляют, но в текущей задачи делать её необязательно
@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['email', 'role']
    readonly_fields = ['last_login', 'password']
    filter_horizontal = []
    list_filter = ['role', 'email']
    list_per_page = 10
    list_max_show_all = 100

# ==================================================================================
# @admin.register(User)
# class MyUserAdmin(UserAdmin):
#     model = User
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
#     readonly_fields = ('last_login', 'date_joined')
#     search_fields = ('username', 'email', 'first_name', 'last_name',)
#     filter_horizontal = ()
#     list_filter = ('is_staff', 'is_active', 'is_superuser', )
#     list_per_page = 10
#     list_max_show_all = 100
