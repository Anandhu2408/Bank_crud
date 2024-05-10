from django.shortcuts import render
from django.http import HttpResponse
from .models import account
from django.urls import reverse_lazy
from .forms import Accountform
from django.contrib.auth import authenticate,login,logout
from django.views.generic import UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required
def view(request):
    a=account.objects.all()
    return render(request, 'view.html',{'a':a})
@login_required
def add(request):
    if(request.method=='POST'):
        n=request.POST['n']
        ac=request.POST['ac']
        ad=request.POST['ad']
        m=request.POST['m']
        b=request.POST['b']
        a=account.objects.create(account_holder=n,account_number=ac,address=ad,mobile_number=m,Account_balance=b)
        a.save()
        return view(request)

    return render(request,'add.html')

class edit(UpdateView):
    model = account
    template_name = "edit.html"
    fields = ['account_holder', 'account_number', 'address', 'mobile_number','Account_balance']
    success_url = reverse_lazy('account:home')


class delete(DeleteView):
    model=account
    template_name = "delete.html"
    success_url=reverse_lazy('account:home')

def register(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        if(cp==p):
            user=User.objects.create_user(username=u,password=p)
            user.save()
            return user_login(request)
        else:
            return HttpResponse("passwords are not same")
    return render(request, 'register.html')
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse("invalid credentials")

    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    # return user_logout(request)
    return render(request, 'home.html')
