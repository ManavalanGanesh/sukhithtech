from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import *
from Trainings.models import Trainingsch, Order

def profile(request):

    current_user = request.user
    print(current_user.id)
    user1 = Order.objects.all()
    context = {
        'userobj': user1
    }

    return render(request, "User/profile.html",context)

def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'User/register.html', {'form': form})

def userreg(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'base.html', {'form': form, 'val': 2})

def logcon(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
    context = {'form': form}
    return render(request, 'base.html', context)

def logging(request):
    obj1 = userlog.objects.get(id=1)
    context = {
        'object': obj1
    }
    return render(request, 'base.html', {'object': obj1})

def usermail(request, x):
    obj1 = User.objects.get(id=x)

    context = {
        'object': obj1
    }
    return render(request, 'base.html', {'object': obj1})




def sendmail(request):
    if request.method == 'POST':
        sendsub = 'password reset mail'
        sendmsg = " your new password is: abcd1245#%&"
        sendmailto = 'manavalanganesh@gmail.com'
        sendmailfrom = 'bvkmanavalan@gmail.com'
        send_mail(sendsub, sendmsg, sendmailfrom, [sendmailto])
        print(User.username)
        User.set_password(User.username, 'abcd1245#%&')
        return render(request, "User/password_reset_sent.html", {'sendmsg': sendmsg})
    else:
        return render(request, 'User/password_reset_sent.html', {})
