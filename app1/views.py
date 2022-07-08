from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from app1.forms import Userform,UserProfileInfoForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def home(request):
    return render(request,"app1/home.html")
@login_required()
def outlog(request):
    logout(request)
    return redirect(reverse('home'))


def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                print('not active')
                return HttpResponse('inactive account')
        else:
            print("fail to log in")
            return HttpResponse('invalid account')
    else:
        return render(request,'app1/login.html')


def register(request):
    user_form  = Userform()
    profile_form = UserProfileInfoForm()
    registered=False

    if request.method =='POST':
        user_form = Userform(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
        
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered=True
            return render(request,"app1/registration.html",
                context={'user_form':user,
                        'profile_form':profile,
                        'registered':registered})
        else:
            print(user_form.errors,profile_form.errors)
    else:   
        return render(request,"app1/registration.html",
                        context={'user_form':user_form,
                                'profile_form':profile_form,
                                'registered':registered})


