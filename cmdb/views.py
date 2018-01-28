from django.shortcuts import render
from cmdb import models

# Create your views here.
from django.shortcuts import HttpResponse
user_list=[
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"},
]
def index(request):

    if request.method=="POST":
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        email=request.POST.get("eml",None)

        user_list=models.UserInfo.objects.create(user=username,pwd=password,eml=email)
    user_list=models.UserInfo.objects.all()
    return  render(request,"index.html",{"data":user_list})