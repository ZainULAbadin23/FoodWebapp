from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def admin_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"
):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def manager_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_manager or u.is_superuser or u.is_resturant,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def resturant_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"
):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_resturant,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def deliverer_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"
):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_deliverer,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def customer_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"
):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_customer,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def staff_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"
):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff or u.is_manager or u.is_superuser or u.is_resturant,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator