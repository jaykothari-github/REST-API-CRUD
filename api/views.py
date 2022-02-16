from urllib.request import Request
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import * 


# Create your views here.

@api_view(['GET'])
def overview(request):
    api_urls = {
        'Overview' : '/',
        'All Data' : '/all-data/',
        'Create Todo' : '/create-data/',
        'One Data' : '/one-data/id',
        'Update Data' : '/update-data/id',
        'Delete Data' : '/delete-data/id',
    }
    return Response(api_urls)

@api_view(['GET'])
def all_data(request):
    todos = TODO.objects.all()
    serializer = TodoSerializer(todos,many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def create_data(request):
    if request.method == 'POST':
        serializers = TodoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
    data = {
        "id": 'id',
        "task": "Task Title",
        "details": "Details of task",
        "status": 'true or false'
    }
    return Response(data)

@api_view(['GET'])
def one_data(request,pk):
    todo = TODO.objects.get(id=pk)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def update_data(request,pk):
    todo = TODO.objects.get(id=pk)
    if request.method == 'PUT':
        serializers = TodoSerializer(todo,data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)


@api_view(['GET','Delete'])
def delete_data(request,pk):
    if request.method == 'DELETE':
        try:
            todo = TODO.objects.get(id=pk)
            todo.delete()
            return Response('DATA Deleted')
        except:
            return Response('Invalid Id')
    else:
        try:

            todo = TODO.objects.get(id=pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        except:
            return Response('Data not found')

    
    