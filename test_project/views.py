from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render
from django.template.context_processors import csrf
from django.views import View

from test_project.forms import UserRegForm, UserLoginForm
from url_monitor.models import Url


class Reg(View):

    def get(self, request):
        context = {}
        context.update(csrf(request))
        context['form'] = UserRegForm()
        return render(request, 'reg.html', context=context)

    def post(self, request):
        form = UserRegForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            # TODO just test. remove later
            user.is_staff = True
            user.save()
            content_type = ContentType.objects.get_for_model(Url)
            permission_list = Permission.objects.filter(
                codename__contains='_url',
                content_type=content_type,
            )
            user.user_permissions.set(permission_list)

            login(request, user)
            return redirect('base')
        error_msg = form.errors
        return render(request, 'reg.html', context={'error_msg': error_msg})


class Login(View):

    def get(self, request):
        context = {}
        context.update(csrf(request))
        context['form'] = UserLoginForm()
        return render(request, 'login.html', context=context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('base')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('base')