from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from user.forms import UserCreationForm
from user.models import CustomUser


class DelivererSignupForm(UserCreationForm):
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
            attrs={"class": "form-control", "placeholder": "First Name"}
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
            "phone",
            "password1",
            "password2",
        )

    def save(self):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_deliverer = True
        user.save()
        return user
