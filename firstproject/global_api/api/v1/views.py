from one.serializers import FruitsSerializer,UserSerializer
from one.models import Fruits
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView,status
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsOwner
from django.http import Http404

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =[permissions.IsAuthenticated,IsOwner]

class FruitsListView(generics.ListAPIView):
    queryset = Fruits.objects.all()
    serializer_class = FruitsSerializer  

class FruitsUpdateView(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = Fruits.objects.all()
    serializer_class = FruitsSerializer  


    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

#function basaed api views
@api_view(['POST','GET'])

def fruit_list(request,):
    """
    List all code snippets, or create a new snippet.
    """
    try :
        fruit = Fruits.objects.all()
    except Fruits.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)    
    if request.method == 'GET':
        fruits  = Fruits.objects.all()
        serializer = FruitsSerializer(fruits, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = FruitsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        serializer = FruitsSerializer(fruit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

@api_view(['GET','PUT','DELETE'])
def fruit_detail(request, pk):
    
    try:
        fruit = Fruits.objects.get(pk=pk)
    except Fruits.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FruitsSerializer(fruit)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = FruitsSerializer(fruit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        fruit.delete()
        return HttpResponse(status=204)        