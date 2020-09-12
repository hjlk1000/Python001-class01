from django.shortcuts import render
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
    if request.method == 'GET':
        login_form = LoginForms()
        return render(request, 'login_form.html', {'form': login_form})
    elif request.method == 'POST':
        login_form = LoginForms(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')