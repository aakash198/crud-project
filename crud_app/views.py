from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from crud_app.models import student
# Create your views here.
def index(request):
    if(request.method=='POST'):
        name=request.POST['nm']
        address=request.POST['addr']
        city=request.POST['city']
        phone_no=request.POST['mbl']
        m=student(name=name,address=address,city=city,phone_no=phone_no)
        m.save()
        # k=student.objects.all()
        # return render(request,'index.html',{'kmn':k})
        return redirect('/')
    else:
        k=student.objects.all()
        return render(request,'index.html',{'kmn':k})

def update(request,id):
    if(request.method=='POST'):
        name=request.POST['nm']
        address=request.POST['addr']
        city=request.POST['city']
        phone_no=request.POST['mbl']
        student.objects.update(name=name,address=address,city=city,phone_no=phone_no)
        return redirect('/')
    else:
        mn=student.objects.get(id=id)
        return render(request,'update.html',{'val':mn})

def delete(request,id):
    sm=student.objects.get(id=id)
    sm.delete()
    return redirect("/")