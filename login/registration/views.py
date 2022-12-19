from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
# Create your views here.

def HomePage(request):
    return render(request,"home.html")


def SignUp(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        # print(uname,email,pass1,pass2)
        if pass1!=pass2:
            return HttpResponse("Your Password and confirm is not same")
        else:

            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,"signup.html")


def LogIn(request):
    return render(request,"login.html")
