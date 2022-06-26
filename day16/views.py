from django.shortcuts import render,redirect
from day16 import models

# import pandas
# import joblib
# path="../modeltest1/X_test.csv"
# p = joblib.load("../modeltest1/model/test1.model")
# X_test = pandas.read_csv(path)
# print(X_test)
# predict=p.predict(X_test)
# print(predict)
# Create your views here.
def depart_list(request):
    depart = models.deparment.objects.all()
    return render(request, 'depart/depart_list.html',{'depart':depart})

def depart_list_add(request):
    if(request.method=="POST"):
        models.deparment.objects.create(title=request.POST.get("title"),ID=request.POST.get("ID"))
        return redirect('/depart_list')
    else:
        return render(request,'depart/depart_list_add.html')

def delete(request):
    id = request.GET.get("ID")
    models.deparment.objects.filter(ID=id).delete()
    print(id)
    return redirect('/depart_list')

def edit(request,nid):
    if(request.method=="GET"):
        query = models.deparment.objects.filter(ID=nid).first()
        return render(request,"depart/depart_list_edit.html",{'obj':query})
    else:
        models.deparment.objects.filter(ID=nid).update(ID=request.POST.get("ID"),title = request.POST.get("title"))
        return redirect("/depart_list")