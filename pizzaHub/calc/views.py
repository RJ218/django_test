from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieInfo



# Create your views here.
def home(request):
    return render(request, 'user_login.html');

def display(request):

    #movie_obj = MovieInfo()
    movie_name=request.GET['movie_name']
    movie_img=request.GET['movie_image']
    movie_descrip=request.GET['movie_description']
    movie_createdate=request.GET['movie_createdate']
    movie_releasedate=request.GET['movie_releasedate']
    #MovieList.append(movie_obj)

    movie_list=MovieInfo(movie_name=movie_name,movie_img=movie_img,movie_createdate=movie_createdate,movie_releasedate=movie_releasedate,movie_descrip=movie_descrip)
    movie_list.save()

    all_movie=MovieInfo.objects.all()

    
    return render(request , 'movie_list.html',{'movielist':all_movie});