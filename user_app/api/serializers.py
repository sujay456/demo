from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterationSerializer(serializers.ModelSerializer):
    
    password2=serializers.CharField(write_only=True,style={'input_type':'password'})
    
    class Meta:
        model=User
        fields =['username', 'password', 'email','password2']
        
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        
        p1=self.validated_data['password']
        p2=self.validated_data['password2']
        
        if p1!=p2:
            raise serializers.ValidationError({'error':"Passwords do not match"})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        
        account=User(email=self.validated_data['email'],username=self.validated_data['username'])
        
        account.set_password(p1)
        
        account.save()
        
        return account
        
        
        

        