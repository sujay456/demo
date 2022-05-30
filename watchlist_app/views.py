# from django.shortcuts import render,HttpResponse

# from django.http import JsonResponse
# from .models import Movie

# # Create your views here.

# def movie_list(request):
    
#     movies=Movie.objects.all()
    
#     data={
#         'movies':list(movies.values())
#         }
    
#     return JsonResponse(data)

# def movie_detail(request,pk):
#     movie=Movie.objects.get(pk=pk)
    
#     print(movie)
#     # here we have a burden of sending each items manually , hence we can use django rest framework
    
    
#     # mapping in drf is done by serialization
#     data={
#         'name':movie.name,
#         'description':movie.description,
#         'active':movie.active 
#     }
#     return JsonResponse(data)
    