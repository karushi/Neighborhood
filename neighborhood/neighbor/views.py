from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import  Neighbourhood,Business,User,Post

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    name = Neighbourhood.objects.all()
    return render(request,'index.html',{"title":title,"name":name})