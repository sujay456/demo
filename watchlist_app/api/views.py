from rest_framework import status
from watchlist_app.models import WatchList,StreamPlatform,Review
from .serializer import WatchSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


from rest_framework.permissions import IsAuthenticated
from .permission import IsAdminorReadonly,ReviewUserorReadonly

# from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

# with concrete /generics

class ReviewCreate(generics.CreateAPIView):
    
    serializer_class=ReviewSerializer
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk=self.kwargs['pk']
        
        watchlist=WatchList.objects.get(pk=pk)
        
        review_user=self.request.user
        review_queryset=Review.objects.filter(watchlist=watchlist,review_user=review_user)
        if review_queryset.exists():
            # we have a problem
            raise ValidationError("You have already posted a review")
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (serializer.validated_data['rating']+watchlist.avg_rating)/2 
        
        watchlist.number_rating=watchlist.number_rating+1
        watchlist.save()
        serializer.save(watchlist=watchlist,review_user=review_user)
        
    
class ReviewList(generics.ListCreateAPIView):
    
    # queryset = Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]
    # here we have overrided the default querset
    def get_queryset(self):
        pk=self.kwargs['pk']
        # kwargs is keword argument
        
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    
    permission_classes=[ReviewUserorReadonly]
    # permission_classes=[IsAuthenticated]

# with mixins 
# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
     

# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class StreamPlatformAV(APIView):
    
    def get(self, request):
        streamplatform = StreamPlatform.objects.all()
        
        serializer= StreamPlatformSerializer(streamplatform,many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer= StreamPlatformSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class SteamDetailAV(APIView):
    def get(self, request,pk):
        
        stream=StreamPlatform.objects.get(pk=pk)
        
        serializer=StreamPlatformSerializer(stream)
        
        return Response(serializer.data)
    
    def put(self,request,pk):
        
        stream=StreamPlatform.objects.get(pk=pk)
        
        serializer=StreamPlatformSerializer(stream,data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors) 
        
    def delete(self,request,pk):
        
        stream=StreamPlatform.objects.get(pk=pk)
        
        stream.delete()       
        return Response(status=status.HTTP_204_NO_CONTENT)


# we dont have to have any decorators here .
class WatchListAV(APIView):
    
    def get(self,request):
        movies=WatchList.objects.all()
        
        serializer = WatchSerializer(movies,many=True)

        return Response(serializer.data)
    
    def post(self,request):
        
        serializer = WatchSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchDetailAV(APIView):
    
    def get(self, request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=WatchSerializer(movie)
        
        return Response(serializer.data)
    def put(self, request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchSerializer(movie,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        
        movie.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

# @api_view(['GET','POST'])
# def movie_list(request):
    
#     if request.method == 'GET':            
#         movies=Movie.objects.all()
        
#         serializer = MovieSerializer(movies,many=True)
        
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,pk):
#     if request.method == 'GET':
#         movie=Movie.objects.get(pk=pk)
        
#         serializer=MovieSerializer(movie)
        
#         return Response(serializer.data)

#     if request.method == 'PUT':  #in put we update every feild , but in patch we update only specified feild
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         movie=Movie.objects.get(pk=pk)
        
#         movie.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        