from django.contrib import admin
from movies.models import Movie

@admin.register(Movie)
class ActorAdmin(admin.ModelAdmin):
    list_disply = ('title', 'genre', 'realease_date','actors','resume',)