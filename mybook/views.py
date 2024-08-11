from django.shortcuts import render
from mybook.models import *
# Create your views here.
def Home(request):
    results=Book.objects.all()
    return render(request,'index.html',{'books':results})


def createAuthor(request):
    if request.method=="POST":
        name=request.POST.get('aname')
        age=request.POST.get('age')
        rating=request.POST.get('rate')
        obj=Author(name=name,age=age,rating=rating)
        obj.save()    
    return render(request,'author.html')


def CreateBook(request):
    if request.method=="POST":
        t=request.POST.get('bname')
        p=request.POST.get('price')
        g=request.POST.get('genre')
        s=request.POST.get('sno')
        if Author.objects.filter(id=s).exists():
            a=Author.objects.get(id=s)
            obj=Book(title=t,price=p,genre=g,author=a)
            obj.save()
    return render(request,'book.html')