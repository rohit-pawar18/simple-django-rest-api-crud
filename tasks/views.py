from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        task_id = request.GET.get('task_id', None)
        if task_id is not None:
            tasks = tasks.filter(id=task_id)
        
        tutorials_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, task_id):
    try:
        task = Tasks.objects.get(pk=task_id)
    except Tasks.DoesNotExist:
        return JsonResponse({'message': 'No task found for given Id!'}, status=status.HTTP_204_NO_CONTENT)
 
    if request.method == 'GET': 
        task_serializer = TaskSerializer(task) 
        return JsonResponse(task_serializer.data) 

    elif request.method == 'PUT': 
        task_data = JSONParser().parse(request) 
        task_serializer = TaskSerializer(task, data=task_data) 
        if task_serializer.is_valid(): 
            task_serializer.save() 
            return JsonResponse(task_serializer.data) 
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE': 
        task.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_comment(request):
    comm_data = JSONParser().parse(request)
    comm_serializer = CommentSerializer(data=comm_data)
    if comm_serializer.is_valid():
        comm_serializer.save()
        return JsonResponse(comm_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(comm_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, Comment_id):
    try:
        comm = Comments.objects.get(pk=Comment_id)
    except Comments.DoesNotExist:
        return JsonResponse({'message': 'No Comment found for given Id!'}, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET': 
        comm_serializer = CommentSerializer(comm) 
        return JsonResponse(comm_serializer.data) 

    elif request.method == 'PUT': 
        comm_data = JSONParser().parse(request) 
        comm_serializer = TaskSerializer(comm, data=comm_data) 
        if comm_serializer.is_valid(): 
            comm_serializer.save() 
            return JsonResponse(comm_serializer.data) 
        return JsonResponse(comm_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        comm.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    