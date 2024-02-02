from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from phonenumber_field.formfields import PhoneNumberField

from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class MyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ["username", "password"]:
            self.fields[fieldname].widget.attrs = {"class": "form-control",
                                                   "placeholder": fieldname}


class AdminSignupForm(UserCreationForm):
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
        user.is_superuser = True
        # user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class ManagerSignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "User Name"}
        ),
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
    phone = PhoneNumberField(
        region='PK',
        widget=PhoneNumberPrefixWidget(initial="PK",
                                       country_choices=[("PK", "Pakistan")],
                                       attrs={"class": "form-control",
                                              "maxlength": 11,
                                              "blank": "True"
                                              },),
        required=False,
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
        user.is_manager = True
        user.is_staff = True
        user.save()
        return user


class CustomerSignupForm(UserCreationForm):
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
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial="PK", attrs={
            "class": "form-control",
            "maxlength": 11,
            "blank": "True",
            },
        ),
        required=False,
        )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "password1",
            "password2",
        )

    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user


# class PurchaserAddForm(forms.ModelForm):
#     phone = PhoneNumberField(
#         widget=PhoneNumberPrefixWidget(
#             initial="PK",
#             attrs={
#                 "class": "form-control",
#                 "maxlength": 11,
#                 },

#             ),
#             required=False,

#     )

#     class Meta:
#         model = Purchaser
#         fields = "__all__"

#         widgets = {
#             "person_name": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                 }
#             ),
#             "company_name": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                 }
#             ),
#             "email": forms.EmailInput(attrs={"class": "form-control"}),
#             "address": forms.Textarea(
#                 attrs={
#                     "class": "form-control",
#                 }
#             ),
#         }


# class CustomerAddForm(forms.ModelForm):
    
#     phone = PhoneNumberField(
#         widget=PhoneNumberPrefixWidget(
#             initial="PK",
            
#             attrs={
#                 "class": "form-control",
#                 "maxlength": 11,
#                 "blank": "True",
#                 },
#             ),
#             required=False,

#     )

#     class Meta:
#         model = Customer
#         fields = "__all__"

#         widgets = {
#             "person_name": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "Full Name",
#                 }
#             ),
#             "email": forms.EmailInput(attrs={"class": "form-control","placeholder": "someone@example.com"}),
#             "address": forms.Textarea(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "Customer's Address",
#                 }
#             ),
#         }