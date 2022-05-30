from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
from django.contrib.auth.models import User
# Create your models here.

class StreamPlatform(models.Model):
    
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website=models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    
    title =models.CharField(max_length=50)
    
    description=models.CharField(max_length=200)
    
    active = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    avg_rating=models.FloatField(default=0)
    number_rating=models.IntegerField(default=0)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist",null=True)
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    
    review_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    rating=models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    description=models.TextField()
    
    created=models.DateTimeField(auto_now_add=True)
    
    update=models.DateTimeField(auto_now=True)
    
    active=models.BooleanField(default=True)
    
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='reviews')
    
    def __str__(self):
        return f"{self.rating}-{self.watchlist.title}"