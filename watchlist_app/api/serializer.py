from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review



class ReviewSerializer(serializers.ModelSerializer):
    
    
    review_user=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Review
        # fields="__all__"
        exclude=['watchlist']


class WatchSerializer(serializers.ModelSerializer):
    
    reviews=ReviewSerializer(many=True,read_only=True)
    
    class Meta:
        model=WatchList
        fields="__all__"
        # exclude=[]


class StreamPlatformSerializer(serializers.ModelSerializer):
    
    # this variable name is same as we specified in the models related_name
    watchlist=WatchSerializer(many=True,read_only=True)
    # watchlist=serializers.StringRelatedField(many=True)
    # watchlist=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # watchlist=serializers.HyperlinkedRelatedField(
    #     many=True,read_only=True,
    #     view_name="movie_detail"
    # )
    class Meta:
        model=StreamPlatform
        
        fields="__all__"  
    








# -------------------------------------------------------------------------
# validators
# def name__length(value):
#     if len(value) <2 :
#         raise serializers.ValidationError("Name is too short")
#     else:
#         return value
    
# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name__length])
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         # instance is the old instance
#         # validated_data is the new instance
#         instance.name = validated_data.get('name',instance)
#         instance.description = validated_data.get('description',instance)
#         instance.active = validated_data.get('active',instance)
#         instance.save()
#         return instance
#     # object level validation
    
#     def validate(self,data):
        
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Ttitle and description must not be same")
#         else:
#             return data;    
#     # this is field level validation
#     # def validate_name(self,value):
        
#     #     if len(value) <2 :
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return value
    
    
    
# # -----------------------------------------
# def get_name_len(self,object):
#         return len(object.name)
#     # but validation have to be done as below
#     def validate(self,data):
        
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Ttitle and description must not be same")
#         else:
#             return data;    
#     # this is field level validation
#     def validate_name(self,value):
        
#         if len(value) <2 :
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return value