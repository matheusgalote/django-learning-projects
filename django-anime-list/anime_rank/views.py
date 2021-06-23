from django.shortcuts import render
from .models import Anime

# Create your views here.
def anime_rank(request):
    animes = Anime.objects.all().order_by('-grade')
    context = {
        'animes': animes,
    }
    return render(request, 'rank_anime.html', context)

def anime_detail(request, pk):
    anime = Anime.objects.get(pk=pk)
    context = {
        'anime': anime
    }
    return render(request, "anime_detail.html", context)