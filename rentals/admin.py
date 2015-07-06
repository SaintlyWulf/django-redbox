from django.contrib import admin
from .models import Movie, Person

class ActorInline(admin.TabularInline):
	model = Person
	extra = 3
	verbose_name = 'Stars' 
	verbose_name_plural = 'Stars'

class MovieAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields':['title', 'summary']}),
		('Release Info',	{'fields':['release_date','rating']}),
		('Bookkeeping',		{'fields':['copies']})
	]
	inlines = [ActorInline]
	list_display = ('title', 'release_date', 'in_stock')
	search_fields = ['title']
		


admin.site.register(Movie, MovieAdmin)

# Register your models here.
