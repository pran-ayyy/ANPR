from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q 
from .forms import *
from django.contrib.auth.models import User
import easyocr as ocr
import random as r
from datetime import datetime, timedelta
from .img_anal import return_plate

# Create your views here.

def introPage(request):
    return render(request, 'base/intro.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username/password')
    context = {'page': 'login'}
    return render(request, 'base/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()
    print(form)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured. Please try again')
    context = {
        'page': 'register',
        'form': form,
    }
    return render(request, 'base/signup.html', context)


@login_required(login_url='login')
def home(request):
    return render(request, 'base/home.html')


@login_required(login_url='login')
def logsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    logs = Log.objects.filter(
        Q(onduty__username__icontains=q) |
        Q(vehicle__plate__icontains=q) |
        Q(loc__icontains=q)
    )
    context = {
        'logs': logs,
        'logs_count': logs.count(),
    }
    return render(request, 'base/logs.html', context)


@login_required(login_url='login')
def createLog(request):
    result = return_plate(r"E:\Vinhack\Practice\practice\base\static\images-car\Cars8.png")
    now = datetime.now()
    exit_time = now + timedelta(minutes=r.randint(60,120))
    vehicle = Vehicle(plate=result, type="CAR")
    vehicle.save()
    log = Log(vehicle=vehicle,
    onduty=request.user, 
    entry=now.strftime("%Y-%m-%d %H:%M:%S"),
    exit=exit_time.strftime("%Y-%m-%d %H:%M:%S"),
    loc=r.choice(["VELLORE", "BANGLORE", "CHENNAI"]))
    log.save()
    return redirect('logs')

    # form = LogForm()
    # if request.method == 'POST':
    #     form = LogForm(request.POST)
    #     if form.is_valid():
    #         log = form.save(commit=False)
    #         log.onduty = request.user
    #         log.save()
    #         return redirect('home')
    # context = {'form': form, }
    # return render(request, 'base/log_form.html', context)


@login_required(login_url='login')
def vehiclePage(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    context = {
        'vehicle': vehicle,
    }
    return render(request, 'base/vehicle.html', context)


def createVehicle(request, s):
    v = Vehicle(plate=' '.join(s.split()[:-1]), type=s.split()[-1])
    v.save()
    return redirect('create-log')