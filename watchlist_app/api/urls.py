from django.urls import path

from . import views

urlpatterns = [
   path('list/',views.WatchListAV.as_view(),name='movie_list'),
   path('detail/<int:pk>',views.WatchDetailAV.as_view(),name='movie_detail'),
   
   path('stream/',views.StreamPlatformAV.as_view(),name='stream'),
   path('stream/<int:pk>',views.SteamDetailAV.as_view(),name='stream-details'),

   
   # path('review/<int:pk>',views.ReviewDetail.as_view(),name='review-detail'),
   # path('review/',views.ReviewList.as_view(),name='review'),

   path('<int:pk>/review',views.ReviewList.as_view(),name='review-list'),
   path('review/<int:pk>',views.ReviewDetail.as_view(),name='review-detail'),
   path('<int:pk>/review-create',views.ReviewCreate.as_view(),name='review-list'),

]
