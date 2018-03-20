from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import  Neighbourhood,Business,User,Post
from .form import PostForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    name = Neighbourhood.objects.all()
    return render(request,'index.html',{"name":name})


@login_required(login_url="/accounts/login/")
def search_results(request):
    if "business" in request.GET and request.GET['business']:
        search_term = request.GET.get('business')
        searched_name = Business.search_by_business(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,business:searched_name})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message}) 


@login_required(login_url='/accounts/login/')
def edit_user(request):
    title = 'user'
    try:
        
        
        
        
        
        
        
        
        
        user = User.objects.all()
    except User.DoesNotExist:
        raise Http404
    return render(request, 'user.html', {"title":title,"user":user})       


@login_required(login_url='/accounts/login/')
def post(request):
    title = 'neighborhood |post'
    post = Post.get_post()
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.posted_by = post
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        
    return render(request,'post.html',{"title":title,"form":form})