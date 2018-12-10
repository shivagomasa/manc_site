from django.contrib.auth import login,authenticate
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from . forms import UserForm

# Create your views here.
def home_page(request):
    return render(request,'manc_dev/home_page.html')

def about(request):
    detail = get_object_or_404(Post)
    frontend = {'detail':detail}
    return render(request, 'manc_dev/about.html',frontend)

def careers(request):
    detail = get_object_or_404(Post)
    frontend = {'detail':detail}
    return render(request,'manc_dev/careers.html',frontend)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('about')
    else:
        form = UserForm()
    return render(request,'registration/signup.html',{'form':form})