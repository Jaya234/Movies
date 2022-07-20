from rest_framework.response import Response
from rest_framework.decorators import api_view 
from watchlist_app.models import Movie
from watchlist_app.API.serializers import MovieSerializer
# writing a class to access the complete list about my movies
@api_view

def movie_list(request):
    movies = Movie.objects.all() # select all the objects
    serializer = MovieSerializer(movies)
    return Response(serializer.data)
# if u try to print a serializer it is also an object
# so i am going to print all data

@api_view
def movie_detail(request, pk):# it is going to accept an request
    #and also it is going to accept a pk (primary key)
    # store everything for a single object only
    movie = Movie.objects.get(pk= pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    
# get() raises a DoesNotExist exception if an object wasn't found 
# for the given parameters. This exception is an attribute of the 
# model class.

