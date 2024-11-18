from django.shortcuts import render,redirect
from books.models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def viewbooks(request):
    #k=modelname.objects.all()
    k=Book.objects.all()  #(select * from)
    context={'book':k}
    return render(request,'viewbooks.html',context)

@login_required
def addbooks(request):

    if(request.method=="POST"):
        t=request.POST['t']
        a = request.POST['a']
        pr = request.POST['pr']
        pg = request.POST['pg']
        l = request.POST['l']
        c = request.FILES['c']
        pdf = request.FILES['pdf']
        b=Book.objects.create(title=t,author=a,price=pr,pages=pg,language=l,cover=c,pdf=pdf) ##insert into
        b.save()
        return redirect("books:view_books")
    return render(request, 'add.html')

@login_required
def viewdetails(request,p):
    k=Book.objects.get(id=p)  #reads a particular element
    context={'book':k}
    return render(request,'details.html',context)


def delete(request,p):
    k = Book.objects.get(id=p)
    k.delete()
    return redirect("books:view_books")

def edit(request,p):
    k = Book.objects.get(id=p)
    if(request.method=="POST"):
        k.title = request.POST['t']
        k.author = request.POST['a']
        k.price = request.POST['pr']
        k.pages = request.POST['pg']
        k.language = request.POST['l']

        if(request.FILES.get('c')==None):
            k.save()
        else:
            k.cover=request.FILES.get('c')

        if (request.FILES.get('pdf') == None):
            k.save()
        else:
            k.pdf = request.FILES.get('pdf')

        k.save()

        return redirect("books:view_books")

    context={'book':k}

    return render(request, 'edit.html', context)
