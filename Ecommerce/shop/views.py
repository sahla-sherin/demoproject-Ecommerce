from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def categories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'categories.html',context)

def products(request,p):
    c=Category.objects.get(id=p)
    p=Product.objects.filter(category=c)
    context = {'cat': c,'product':p}
    return render(request,'products.html',context)

def details(request,p):
    pro=Product.objects.get(id=p)
    context={'product':pro}
    return render(request,'details.html',context)


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
            return redirect('shop:user_login')
        else:
            return HttpResponse("Passwords are not same")

    return render(request,'userregister.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)

        if user:
            login(request, user)
            return redirect("shop:categories")
        else:
            return HttpResponse("Invalid Credentials")

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('shop:user_login')

def add_category(request):
    if(request.method=="POST"):
        cat=request.POST['cat']
        desc=request.POST['desc']
        img=request.FILES['img']
        c=Category.objects.create(name=cat,desc=desc,image=img)
        c.save()
        return redirect('shop:categories')
    return render(request,'addcategory.html')

def add_product(request):
    if (request.method == "POST"):
        prd = request.POST['prd']
        desc = request.POST['desc']
        img = request.FILES.get('img')
        pr=request.POST['pr']
        st=request.POST['st']
        c=request.POST['c']
        cat=Category.objects.get(name=c)
        p = Product.objects.create(name=prd, desc=desc, image=img,price=pr,stock=st,category=cat)
        p.save()
        return redirect('shop:categories')
    return render(request,'addproduct.html')

def add_stock(request,pr):
    p=Product.objects.get(id=pr)

    if(request.method=="POST"):
        p.stock=request.POST['st']
        p.save()
        return redirect('shop:details',pr) #gives pr to return to the current products details page

    context={'product':p}
    return render(request,'stock.html',context)


def edit(request,i):
    p = Product.objects.get(id=i)
    if (request.method == "POST"):
        p.name = request.POST['prd']
        p.desc = request.POST['desc']
        p.price = request.POST['pr']
        p.stock = request.POST['st']

        if (request.FILES.get('img') == None):
            p.save()
        else:
            p.image = request.FILES.get('img')

        p.save()

        return redirect("shop:details",i)  # goto the home page in return after submission

    context = {'pro': p}

    return render(request, 'editproduct.html', context)


def delete(request,i):
    p=Product.objects.get(id=i)
    p.delete()

    return redirect('shop:categories')
