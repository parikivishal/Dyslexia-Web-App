from django.shortcuts import render, redirect
from .models import userregister
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = userregister.objects.filter(name=username, password=password)
        if users.exists():
            user = users.first()
            request.session['username'] = username
            return redirect('index')
        else:
            return render(request, 'login.html', {'status': 'Incorrect username and password'})
    return render(request,'login.html')
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        userregister.objects.create(name=username, email=email, password=password, mobile = mobile)
        return redirect('login')
    else:
        return render(request, 'register.html', {'status': 'Something went wrong please try again!'})
    return render(request,'register.html')
