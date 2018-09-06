from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Profile,Game,Manga,Project
from .forms import PostForm, GameForm
from django.utils import timezone
import logging,json

logging.basicConfig(level=logging.DEBUG)

def post_list(request):

    profile = Profile.objects.get(name="Vinctusor")
    manga = Manga.objects.all().order_by('name')
    games = Game.objects.all().order_by('name')
    projects = Project.objects.all()
    logging.debug("logging")
    return render(request, "blog/extra_post_list.html", {'profile' : profile , 'mangas' : manga , 'projects' : projects , 'games' : games})

def post_detail(request,name):
    post = get_object_or_404(Manga,name=name)
    return render(request,"blog/post_details.html", {'manga':post})


def manga_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/new_manga.html', {'form': form})


def game_new(request):
    if request.method == "POST":
        form = GameForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = GameForm()
    return render(request, 'blog/new_game.html', {'form': form})


@csrf_exempt
def prova(request):
        data = {'is_taken': 'porca miseria'}
        return HttpResponse(json.dumps(data),content_type="application/json")