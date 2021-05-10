from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import auth

# from .models import Profile
from .models import UploadVideo
from .models import UploadImgMenu
from .forms import UploadMenu

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('menu')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def index(request):
    video = UploadVideo.objects.all()
    template = loader.get_template('index.html')
    context = {
        'video': video,
    }
    return HttpResponse(template.render(context, request))

def menu(request):
    menu1 = UploadImgMenu.objects.filter(user_id=request.user, menu_no=1)
    menu2 = UploadImgMenu.objects.filter(user_id=request.user, menu_no=2)
    menu3 = UploadImgMenu.objects.filter(user_id=request.user, menu_no=3)
    menu4 = UploadImgMenu.objects.filter(user_id=request.user, menu_no=4)
    template = loader.get_template('menu.html')
    context = {
        'menu1' : menu1,
        'menu2' : menu2,
        'menu3' : menu3,
        'menu4' : menu4,
    }
    return HttpResponse(template.render(context, request))

def upload(request):
    if request.method == 'POST':
        menu = UploadImgMenu(user_id = request.user)
        form = UploadMenu(request.POST or None, request.FILES or None, instance= menu)
        if form.is_valid():
            menu.save()
        return redirect('/upload')
    else:
        form = UploadMenu()
    return render(request, 'upload.html', {
        'form' : form,
    })