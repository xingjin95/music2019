from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'mobile', 'qq', 'weChat']
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] = (_('Personal info'),
                    {'fields': ('first_name', 'last_name', 'email', 'mobile', 'qq', 'weChat')})