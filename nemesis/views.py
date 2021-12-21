from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from nemesis.models import Users
from rest_framework_simplejwt.authentication import JWTAuthentication 
from django.contrib.auth import login
from rest_framework.response import Response

from nemesis.serializers import RegFormSerializer, UserSerializer
from rest_framework import status

# FOR REGISTRATION OF USERS-----
class register_view(APIView):
    serializer=RegFormSerializer()
    def post(self, request):
        serializer = RegFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data)

                     
 # AUTHENTICATED USER CAN VIEW ALL USERS DATA ,UPDATE AND DELETE USER    
class users_view(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def list(self,request):
        user=Users.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
   
    def retrieve(self,request,pk=None):
        id=pk
        print("id",id)
        if id is not None:
            user=Users.objects.get(id=id)
            serializer=UserSerializer(user)
            print(user,"user")
            return Response(serializer.data)
    def update(self,request,pk):
        id=pk
        user=Users.objects.get(id=id)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk):
        id=pk
        user= Users.objects.get(id=id)    
        user.delete()
        return Response({'msg':'Data Deleted'})  

        
    



