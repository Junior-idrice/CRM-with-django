from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
# Create your views here.

def home(request):
    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have been login")
            return redirect('home')
        else:
            messages.success(request, "there was an error login in, try again")
            return redirect('home')
    return render(request, 'website/home.html',{
        'records':records
    })

def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logout ')
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username, password=password)
            login(request, user)
            messages.success(request, 'you are good my boy')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'website/register.html',{'form':form})
    return render(request, 'website/register.html',{'form':form})


def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id = pk)
        return render(request,'website/record.html',{
            'record':customer_record
        })
    else:
        messages.success(request,'you must sign in')
        return redirect('home')

def delete(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request,'record deleted ')
        return redirect('home')
    else:
        messages.success(request, 'you must looged in to do this')
        return redirect('home')

def add(request):
    return render(request, 'website/add.html',{})