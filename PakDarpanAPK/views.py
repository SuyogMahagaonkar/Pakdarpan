from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth.models import User
from .form import UserRegisterForm, UpdateUserDetailForm, UserUpdateForm, UserAddressForm, UserAddressForm1
# Create your views here.
from .models import UserDetail
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    template = loader.get_template('main/index.html')  # getting our template
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('main/login.html')

    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save();
                username = form.cleaned_data.get('username')
                usr = User.objects.filter(username=username).first()
                if username.isdigit():
                    UserDetail(user=usr,mobile=username).save()
                else:
                    usr.email = username
                    usr.save()
                    UserDetail(user=usr).save()
                messages.success(request, f'Account is Created for {username}')
                return redirect('login')
        else:
            form = UserRegisterForm()
    #return render(request, 'main/login.html', {'form':form, 'title':'Sign Up'})
    # getting our template
    return HttpResponse(template.render())