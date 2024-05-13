from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *


def index(request):
    songs = Song.objects.all()
    p = Paginator(songs, 2)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'music_app/index.html', context)


def music_detail(request, pk):
    song = Song.objects.get(id=pk)
    context = {'song': song}
    return render(request, 'music_app/music_detail.html', context)


def download_success(request, pk):
    song = Song.objects.get(id=pk)
    song.download_count = song.download_count + 1
    song.save()

    context = {'song': song}
    return redirect("music_app:music_detail", pk=song.id)


def play_success(request, pk):
    song = Song.objects.get(id=pk)
    song.play_count = song.play_count + 1
    song.save()

    context = {'song': song}
    return redirect("music_app:music_detail", pk=song.id)
