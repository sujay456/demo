from multiprocessing.reduction import steal_handle
from tkinter import W
from django.contrib import admin

from .models import WatchList,StreamPlatform,Review

# Register your models here.

admin.site.register(WatchList)  
admin.site.register(StreamPlatform)  

admin.site.register(Review)  