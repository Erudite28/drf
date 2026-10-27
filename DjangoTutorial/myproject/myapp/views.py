from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import Feature
from django.contrib import messages
#from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Joy',
        'age': 19,
        'title': 'Backend Developer',
    }
    return render(request, 'index.html', context)
    #return HttpResponse('Hi')

def index2(request):
    features = Feature.objects.all()
    return render(request, 'index2.html', {'features': features}) 

def Wordcounter(request):
    return render(request, 'Wordcounter.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        email = request.POST['Email']
        password = request.POST['Password']
        password2 = request.POST['Password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            else:
                messages.info(request, 'Your account has been registered')
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/index2')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/index2')