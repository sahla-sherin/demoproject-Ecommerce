from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        fn = request.POST['fn']
        ln = request.POST['ln']
        e = request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=fn,last_name=ln)
            u.save()
            return redirect('users:user_login')
        else:
            return HttpResponse("Passwords are not same")

    return render(request,'userregister.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)

        if user:
            login(request,user)
            return redirect("books:view_books")
        else:
            return HttpResponse("Invalid Credentials")

    return render(request,'login.html')

def viewusers(request):
    k = User.objects.all()
    context = {'user': k}
    return render(request, 'viewuser.html',context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('users:user_login')

