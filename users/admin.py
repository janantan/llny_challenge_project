from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterForm, CustomUserChangeForm
from .models import NetflixUser


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = CustomUserChangeForm
    model = NetflixUser
    list_display = ('email', 'is_staff', 'is_active', 'user_token', 'score', 'first_name', 'last_name', 'user_type')
    list_filter = ('email', 'is_staff', 'is_active', 'user_token', 'score', 'first_name', 'last_name', 'user_type')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'first_name', 'last_name', 'user_type')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'user_type',)
    ordering = ('email', 'first_name', 'last_name', 'user_type',)


admin.site.register(NetflixUser, CustomUserAdmin)