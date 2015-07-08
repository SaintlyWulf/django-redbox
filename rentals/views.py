from django.shortcuts import render
from django.utils import timezone
from .models import Movie

def movie_list(request):
	movies = Movie.objects.all().order_by('title')
	return render(request, 'rentals/movie_list.html', {'movies': movies})

# Create your views here.
