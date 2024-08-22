from django.urls import path

from . import views

app_name = 'music_app'

urlpatterns = [
    # Leave as empty string for base url
    path('', views.index, name="index"),
    path('music_detail/<int:pk>/', views.music_detail, name="music_detail"),
    path('download_success/<int:pk>/', views.download_success, name="download_success"),
    path('play_success/<int:pk>/', views.play_success, name="play_success"),
    path('ajax_add_review/<int:pk>/', views.ajax_add_review, name="ajax_add_review"),
]
