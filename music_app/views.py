from django.shortcuts import render
from .models import *



def index(request):
	songs = Song.objects.all()
	context = {'songs': songs}
	return render(request, 'music_app/index.html', context)

def music_detail(request):
	context = {}
	return render(request, 'music_app/music_detail.html', context)


