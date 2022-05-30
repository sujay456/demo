from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterationSerializer
from rest_framework.authtoken.models import Token
from user_app import models  
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def logout_view(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def registeration_view(request):
    
    if request.method == 'POST':
        
        serializer=RegisterationSerializer(data=request.data)
        
        data={}
        if serializer.is_valid():
            # as we are need some extra things to do , we will override this save function in serializer
            account=serializer.save()
            data['username']=account.username
            data['email']=account.email
            data['response']="Registeration Successfull"
            
            # data['token']=Token.objects.get(user=account).key
            
            refresh = RefreshToken.for_user(account)
            
            # jwt
            data['token']={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            
            return Response(data)
        else:
            return Response(serializer.errors)
