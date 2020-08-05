from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from cart.models import Cart


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('cart')
        else:
            messages.error(request, 'Login Failed!')
            return redirect('login')
    else:
        return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']

    # check if password matches
        if password == con_password:
            # check if username already exist
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already existed')
                return redirect('register')
            else:
                #check if username exist
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already Existed')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
                    user.save()
                    messages.success(request, 'Registration Successful')
                    return redirect('login')
        else:
            return redirect('register')
    else:
        return render (request, 'account/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
