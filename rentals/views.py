from django.shortcuts import render

def movie_list(request):
	return render(request, 'rentals/movie_list.html', {})

# Create your views here.
