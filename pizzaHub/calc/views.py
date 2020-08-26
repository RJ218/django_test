from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieInfo

MovieList=[]

# Create your views here.
def home(request):
    return render(request, 'user_login.html');

def display(request):

    movie_obj = MovieInfo()
    movie_obj.movie_name=request.GET['movie_name']
    movie_obj.movie_img=request.GET['movie_image']
    movie_obj.moie_descrip=request.GET['movie_description']
    movie_obj.movie_createdate=request.GET['movie_createdate']
    movie_obj.movie_releasedate=request.GET['movie_releasedate']
    MovieList.append(movie_obj)
    
    return render(request , 'movie_list.html',{'movielist':MovieList});