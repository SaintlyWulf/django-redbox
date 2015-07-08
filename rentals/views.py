from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Movie

def movie_list(request):
	movies = Movie.objects.all().order_by('title')
	return render(request, 'rentals/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	return render(request, 'rentals/movie_detail.html', {'movie': movie})

# Create your views here.
