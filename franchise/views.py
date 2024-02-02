from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from user.decorators import (manager_required,
                             staff_required,
                             deliverer_required,
                             resturant_required,
                             admin_required)

# Create your views here.


@login_required
@manager_required
def manager_dashboard(request, *args, **kwargs):
    context = {
        'title': 'Manager Dashboard'
    }
    return render(request, 'franchise/manager_dashboard.html', context)


@login_required
@deliverer_required
def deliverer_dashboard(request, *args, **kwargs):
    context = {
        'title': 'Deliverer Dashboard'
    }
    return render(request, 'franchise/deliverer_dashboard.html', context)
