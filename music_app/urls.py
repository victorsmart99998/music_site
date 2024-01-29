from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
	path('music_detail/', views.music_detail, name="music_detail"),


]