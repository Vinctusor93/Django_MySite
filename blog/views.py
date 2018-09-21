
from django.shortcuts import render,get_object_or_404,redirect
from .models import Profile,Game,Manga,Project
from .forms import PostForm, GameForm
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
import logging
import json

logging.basicConfig(level=logging.DEBUG)

def post_list(request, manga=None):

    if request.method == 'POST' and request.is_ajax():
#############################################################################   Manga Ajax Request #######################################################################
        if request.POST['objects'] == 'manga':
            if request.POST['type'] == 'All':
                results = Manga.objects.all().order_by('name')
            else:
                results = Manga.objects.filter(vote=request.POST['type'])
            manga = []
            for m in results:
                manga.append(m.name)
            return HttpResponse(json.dumps({'manga': manga,'type' : 'Manga'}), content_type="application/json")
#############################################################################   Games Ajax Request #######################################################################
        elif request.POST['objects'] == 'game':
            if request.POST['type'] == 'All':
                results = Game.objects.all().order_by('name')
            else:
                results = Game.objects.filter(play_station=request.POST['type'])
            games = []
            for m in results:
                games.append(m.name)
            print(games)
            return HttpResponse(json.dumps({'game': games, 'type' : 'Game'}), content_type="application/json")
    print("post_list")
    profile = Profile.objects.get(name="Vinctusor")
    if manga == None:
        manga = Manga.objects.all().order_by('name')
    games = Game.objects.all().order_by('name')
    projects = Project.objects.all()
    consoles = Game.objects.values('play_station').distinct()
    print(manga)
    return render(request, "post_list.html", {'profile' : profile , 'mangas' : manga , 'projects' : projects , 'games' : games, 'consoles' :consoles})

def manga_details(request,name):
    print("almeno qua ci arrivo")
    post = get_object_or_404(Manga,name=name)
    return render(request,"manga_details.html", {'manga':post})

def game_details(request,name):
    post = get_object_or_404(Game,name=name)
    return render(request,"game_details.html", {'game':post})


def manga_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'new_manga.html', {'form': form})


def game_new(request):
    if request.method == "POST":
        form = GameForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = GameForm()
    return render(request, 'new_game.html', {'form': form})



def create_post(request):
    print("ajax")
    manga = Manga.objects.get(name="Naruto")
    return redirect('post_list', manga=manga)

def update_manga(request, name):
    instance = get_object_or_404(Manga, name=name)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        if(request.POST['name'] != name):
            Manga.objects.get(name=name).delete()
        return redirect('manga_details', name=request.POST["name"])
    return render(request, 'new_manga.html', {'form': form})

def update_game(request, name):
    instance = get_object_or_404(Game, name=name)
    form = GameForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        if(request.POST['name'] != name):
            Game.objects.get(name=name).delete()
        return redirect('game_details', name=request.POST["name"])

    return render(request, 'new_game.html', {'form': form})

def delete_manga(request, name):
    Manga.objects.get(name=name).delete()
    return redirect('post_list')

def delete_game(request, name):
    Game.objects.get(name=name).delete()
    return redirect('post_list')
