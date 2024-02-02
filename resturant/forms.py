from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from django.utils.translation import gettext_lazy as _

from .models import Product, ProductCategory
from user.forms import UserCreationForm
from user.models import CustomUser


class ResturantSignupForm(UserCreationForm):
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(
            initial="PK", attrs={
                "class": "form-control",
                "maxlength": 11,
                "blank": "True",
                },
                ), required=False,
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Your valid email address",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def save(self):
        user = super().save(commit=False)
        user.is_resturant = True
        user.save()
        return user


class ProductCategoryModelForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ["name", "description", "image"]
        labels = {
            "name": _("Category Name"),
            "description": _("Describe category purpose"),
            "image": _("Upload Image"),
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "product_code",
            "product_name",
            "product_category",
            "my_cost",
            "sale_price",
            "description",
            "image",

        ]
        labels = {
            "product_code": _("Product Code"),
            "product_name": _("Product Name"),
            "product_category": _("Category"),
            "my_cost": _("My Cost"),
            "sale_price": _("Sale Price"),
            "description": _("Description"),
            "image": _("Upload Image"),
        }
        error_messages = {
            "product_code": {
                "max_length": _("This Product's Code is too long."),
            },
            "product_name": {
                "max_length": _("This Product's name is too long."),
            },
            "description": {
                "max_length": _("This Product's name is too long."),
            },
        }
        widgets = {
            "product_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Unique Code",
                }
            ),
            "product_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Product Name",
                }
            ),
            "product_category": forms.Select(
                attrs={
                    "class": "form-control",
                    }),
            "distributor": forms.Select(
                attrs={
                    "class": "form-control",
                    }),
            "my_cost": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "name": "p_price",
                    "placeholder": "Rs.0000",
                }
            ),
            "sale_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "name": "s_price",
                    "placeholder": "Rs.0000",
                }
            ),
            
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your Product Details...",
                }
            ),
        }