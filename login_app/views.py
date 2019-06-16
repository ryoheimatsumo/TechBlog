from django.shortcuts import render
from login_app.forms import UserForm,UserProfileInfoForm

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from blog_app import views as blog_app_views


# Create your views here.
def index(request):
    return render(request,'login_app/index.html')

@login_required
def special(request):
    return render(request,'blog_app/school_list.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registerd=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()

            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:

                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registerd=True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'login_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registerd':registerd})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("blog_app:list"))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username:{} and password{}".format(username,password))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request,'login_app/login.html',{})
