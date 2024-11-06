from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def home(request):
    context = {}
    return render(request, 'real_estate_app/home.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            
            return render(request, 'real_estate_app/login.html', {'error': 'Invalid username or password'})

    return render(request, 'real_estate_app/login.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)  
            return redirect('home')  
    else:
        form = UserCreationForm()

    return render(request, 'real_estate_app/signup.html', {'form': form})
