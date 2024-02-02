from django.urls import path

from .views import manager_dashboard, deliverer_dashboard

urlpatterns = [
    path('manager/dashboard/', manager_dashboard, name="manager-dashboard"),
    path('deliverer/dashboard/', deliverer_dashboard, name="deliverer-dashboard"),
]
