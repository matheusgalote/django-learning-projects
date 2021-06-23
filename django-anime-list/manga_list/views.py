from django.shortcuts import render
from .models import Manga

# Create your views here.
def manga_index(request):
    mangas = Manga.objects.all().order_by('-grade')
    context = {
        'mangas': mangas
    }
    return render(request, 'manga_index.html', context)

def manga_detail(request, pk):
    manga = Manga.objects.get(pk=pk)
    context = {
        "manga": manga,
    }
    return render(request, "manga_detail.html", context)
