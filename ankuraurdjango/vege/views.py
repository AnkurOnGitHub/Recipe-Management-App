from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')     # 'recceipe_name' is the attributes in the input field of html files
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        #To save the data in the model
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        return redirect('/receipes/')
    
    return render(request, 'receipes.html')


@login_required(login_url="/login/")
def receipes_list(request):
    receipes1 = Receipe.objects.all()
    return render(request, 'receipes_list.html', {'receipes1':receipes1})

@login_required(login_url="/login/")
def delete_receipe(request, id):
    Receipe.objects.get(id = id).delete()
    return redirect('/receipes_list/')

@login_required(login_url="/login/")
def update_receipe(request, id):
    singleQuery = receipe = Receipe.objects.get(id = id)                        #fetching the object to update things by the help of (id)
    if request.method == "POST":                                                # if post then only perform thiese task
        data = request.POST                                                     # data used to take the information from front-end
        receipe_name = data.get('receipe_name')                                 # 'receipe_name' is the attributes(name) in the input field of html files 
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        singleQuery.receipe_name = receipe_name
        singleQuery.receipe_description = receipe_description
        if receipe_image:
            singleQuery.receipe_image = receipe_image
        singleQuery.save()
        return redirect('/receipes_list/')
    return render(request, 'receipe_update.html', {'receipe':receipe})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login/')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "Invalid password")
            return render(request,'login.html')
        
        else:
            login(request,user)
            return redirect('/receipes/')
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "username already taken")
            return redirect('/register/')
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")
        return redirect('/register/')
    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')