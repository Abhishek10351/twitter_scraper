from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrape_twitter, name='twitter-scraper'),
]
