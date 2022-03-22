from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages

from auction.forms import *
from auction.models import *


@login_required(login_url = 'login')
def home(request):
    rounds = Round.objects.all()

    phase = Phase.objects.get(pk = 1)
    roundCount = Round.objects.all().count()
    strRound = roundCount + 1

    if request.method == 'POST':
        try:
            auction = Round.objects.create(phase = phase, roundName = strRound, actionStatus = True, end_time = datetime.datetime.today() + datetime.timedelta(minutes = 3))
            auction.save()
            return redirect('home')
        except Exception as e:
            messages.error(request, str(e))

    context = {
        'rounds' : rounds,
    }
    return render(request, 'auction/index.html', context)





## LOGIN
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)    
            return redirect('home')

        else:
            messages.error(request,'User name or password is incorrect.')
            

    context = {}
    return render(request, 'auction/login.html',context)


## LOGOUT
def logout_user(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def changepassword(request):
    headerText = 'Change Password'

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password changed successfully.')
            return redirect('home')
        
    else:
        form = ChangePasswordForm(request.user)

    context = {
        'form' : form,
        'headerText' : headerText,
    }  
    return render(request, 'auction/entry.html', context)




def auctionstart(request):
    phase = Phase.objects.get(pk = 1)
    rounds = Round.objects.all().count()
    strRound = rounds + 1

    if request.method == 'POST':
        try:
            auction = Round.objects.create(phase = phase, roundName = strRound, auctionStatus = True)
            auction.save()
            return redirect('home')
        except Exception as e:
            messages.error(request, str(e))

    context = {

    }
    return render(request, 'auction/index.html', context)
