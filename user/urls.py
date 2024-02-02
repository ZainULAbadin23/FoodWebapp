
from django.urls import path, reverse_lazy

# from .views import management_login
from django.contrib.auth.views import LogoutView

from .views import ManagementLoginView
from .forms import MyLoginForm
urlpatterns = [
    path("login/",
         ManagementLoginView.as_view(
            template_name="user/management_login.html",
            authentication_form=MyLoginForm,
            ), name="login", ),
    path(
        "logout/",
        LogoutView.as_view(
            template_name="user/logout.html",
            next_page=reverse_lazy("home")
        ),
        name="logout",
    ),
]
