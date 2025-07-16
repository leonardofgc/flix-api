from django.db import models
from actors.models import Actor
from genres.models import Genre

class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')  
    """ 
        ForeignKey estabelece um relacionamento de "um-para-muitos", um gênero pode ter vários filmes associados.
        Cada filme tem exatamente um gênero.
        O parâmetro on_delete=models.PROTECT significa que você não pode deletar um gênero enquanto houver filmes associados a ele.
        O related_name='movies' permite acessar todos os filmes de um gênero usando genre.movies.all()
    """
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    """
        Este é um campo ManyToManyField que estabelece um relacionamento de "muitos-para-muitos":
        Um filme pode ter vários atores
        Um ator pode estar em vários filmes
        O Django cria automaticamente uma tabela intermediária para gerenciar estas relações
        O related_name='movies' permite acessar todos os filmes de um ator usando actor.movies.all()
    """

    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
