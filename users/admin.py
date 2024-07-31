from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea, CharField
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


# Personalizar el panel de admin para CustomUser
class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ("email", "username", "first_name", "last_name")
    list_filter = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )
    ordering = ("-date_joined",)
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("Personal", {"fields": ("about",)}),
    )
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(CustomUser, UserAdminConfig)
