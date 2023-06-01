from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import cric
from .forms import cricform


# Create your views here.
def bat(request):
    cricketer=cric.objects.all()
    cricvar={
        'cricketer_list':cricketer
    }
    return render(request,'index.html',cricvar)
def detail(request,cricketer_id):
    cricketer=cric.objects.get(id=cricketer_id)
    return render(request,"detail.html",{'cricketer':cricketer})
def add_cricketer(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        about= request.POST.get('about')
        age= request.POST.get('age')
        img= request.FILES['img']
        cricketer=cric(name=name,about=about,age=age,img=img)
        cricketer.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    cricketer=cric.objects.get(id=id)
    form=cricform(request.POST or None,request.FILES,instance=cricketer)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'cricketer':cricketer})

def delete(request,id):
    if request.method=='POST':
        cricketer=cric.objects.get(id=id)
        cricketer.delete()
        return redirect('/')
    return render(request,'delete.html')

