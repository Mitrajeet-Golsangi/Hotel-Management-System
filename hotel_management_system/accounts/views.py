from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth

from .models import *

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.


def guest_register(request):

    if request.method == "POST":
        
        email = request.POST.get('email')
        name = request.POST.get('fullname')
        password = request.POST.get('password')

        id_proof = request.POST.get('id_proof')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        phn = request.POST.get('phone_number')
        
        user = User.objects.create_user(
            username = email,
            first_name = name,
            email = email,
            password = password,
        )
        user.save()
        
        guest = Guest( 
            id_proof=id_proof,
            age=age,
            sex=sex,
            phone_number=phn
        )
        
        guest.user = user
        
        guest.save()

        return redirect('login')
    else:
        return render(request, 'auth/guest_register.html')


def staff_register(request):
    return render(request, 'auth/staff_register.html')

def signIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid User Credentials!")
            return redirect('login')
    return render(request, 'auth/signIn/signin.html')

@login_required()
def logout(request):
    auth.logout(request)
    return redirect('home')