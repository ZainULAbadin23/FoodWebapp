from django.shortcuts import render
from django.contrib.auth.views import LoginView
# Create your views here.


def management_login(request, *args, **kwargs):
    context = {
        'title': 'Management-login'
    }
    return render(request=request,
                  template_name='user/management_login.html',
                  context=context)


class ManagementLoginView(LoginView):
    template_name = 'user/management_login.html'

    def get_success_url(self) -> str:
        print(self.request.user.is_manager)
        if (self.request.user.is_superuser):
            url = '/admin'
        elif (self.request.user.is_manager):
            url = '/franchise/manager/dashboard/'
        elif (self.request.user.is_deliverer):
            url = '/franchise/deliverer/dashboard/'
        elif (self.request.user.is_resturant):
            url = '/resturant/dashboard/'
        else:
            url = '/'
        return url
