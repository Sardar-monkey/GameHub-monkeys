from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def main(request):
    guides = GuideDesc.objects.all().order_by('-date')[:3]
    context = {
        'guides' : guides
    }
    return render(request, "./main.html", context)


def all_games(request):
    categories = GameCategory.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, "./allgames.html", context)


def all_guides(request):
    guides = GuideDesc.objects.all().order_by('-date')
    context = {
        'guides' : guides
    }
    return render(request, "./allguides.html", context)


def guides_by_cat(request, slug):
    gamecategory = get_object_or_404(GameCategory, slug=slug)
    guidedesc = GuideDesc.objects.filter(category=gamecategory)
    context = {
        'gamecategory' : gamecategory,
        'guidedesc' : guidedesc
    }

    return render(request, "./guidesbycat.html", context)


def guide_desc(request, pk):
    guide_description = get_object_or_404(GuideDesc, pk=pk)
    context = {
        'guide_description' : guide_description
    }

    return render(request, "./guidedesc.html", context)


@login_required
def my_guides(request):
    guides = GuideDesc.objects.filter(author=request.user).order_by('-date')
    context = {
        'guides' : guides
    }
    return render(request, "./myguides.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            guide = form.save(commit=False)
            guide.author = request.user
            guide.save()
            return redirect('my_guides')
    
    else:
        form = CreateForm()

    return render(request, './create.html', {'form':form})


@login_required
def delete_guide(request, pk):
    guide = get_object_or_404(GuideDesc, pk=pk)
    if request.method == "POST":
        if guide.author == request.user:
            guide.delete()
            return redirect('my_guides')


def sign_up(request):   
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = UserForm()

    return render(request, './signup.html', {'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main') 
    else:
        form = AuthenticationForm()

    return render(request, "./login.html", {'form':form})


def logout_action(request):
    logout(request)
    return redirect('main')


def sorry(request):
    return render(request, "./sorry.html")

