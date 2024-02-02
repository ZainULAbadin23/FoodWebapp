from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "username",
        "last_name",
        "email",
        "is_staff",
        "is_manager",
        "is_deliverer",
        "is_resturant",
        "is_customer",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {"fields": ("username",
                        "first_name",
                        "last_name",
                        "email",
                        "password"
                        )},
        ),
        ("Permissions", {"fields": (
            "is_staff",
            "is_manager",
            "is_deliverer",
            "is_resturant",
            "is_customer",
            "is_active",
            )}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_manager",
                    "is_deliverer",
                    "is_resturant",
                    "is_customer",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
