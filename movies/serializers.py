from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all()
    )
    realease_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(), many=True
    )
    resume = serializers.CharField()

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):

        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        """ reviews  = obj.reviews.all()
        if reviews:
            points = 0
            for review in reviews:
                points += review.stars
            total_reviews = reviews.count()

            return round(points / total_reviews,1)
        return None """

    def validate_release_date(self, release_date):
        if release_date.year < 1990:
            raise serializers.ValidationError('Data de lançamento inválida')
        return release_date
    
    def validate_resume(self, resume):
        if len(resume) > 200:
            raise serializers.ValidationError('Resumo deve possuir no máximo 200 caracteres.')
        return resume