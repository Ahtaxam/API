from myapi.serializers import TodoSerializers
from myapi.models import TODO
from django.shortcuts import render
from rest_framework import serializers, status

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_route(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def get_todo(request):
    todos = TODO.objects.all()
    serializer = TodoSerializers(todos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_todo_id(request, pk):
    try:
        todos = TODO.objects.get(id=pk)
        serializer = TodoSerializers(todos, many=False)
        return Response(serializer.data)
    except TODO.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_todo(request, pk):
    todo = TODO.objects.get(id=pk)
    serializer = TodoSerializers(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    todo = TODO.objects.get(id=pk)
    todo.delete()
    return Response("Deleted Successfully")


@api_view(['POST'])
def add_todo(request):
    data = request.data
    todo = TODO.objects.create(
        title=data['title'], desc=data['desc'], date=data['date'])
    serializer = TodoSerializers(todo, many=False)
    print(data)
    return Response(serializer.data)
