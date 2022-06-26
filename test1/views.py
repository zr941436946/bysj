from django.http import HttpResponse
from django.shortcuts import render, redirect
from test1.models import user_list
# Create your views here.
def index(req):
    return render(req, "depart/depart_list.html", )

def userList(req):
    userlist = user_list.objects.all()
    return render(req,"userList.html",{"userlistt":userlist})

def login(req):
    if req.method=="GET":
        return render(req,"login.html")
    else:
        print(req.POST)
        return HttpResponse("登录成功")

def user_add(request):
    if request.method=="GET":
        return render(request,"user_add.html")
    else:
        name = request.POST.get("name")
        password = request.POST.get("password")
        age = request.POST.get("age")
        user_list.objects.create(name=name,password=password,age=age)
        return redirect("/userList",{"xh":"成功添加"})

def user_delete(request):
    id = request.GET.get("id")
    user_list.objects.filter(id=id).delete()
    return redirect("/userList")


