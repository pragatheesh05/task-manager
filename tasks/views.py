from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
from rest_framework import viewsets
from .models import Task, Profile
from .serializers import TaskSerializer, ProfileSerializer

class TaskListCreate(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("---------",request.data)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class profile(APIView):
    def get(self,request):
        profileList = Profile.objects.all()
        profiles = ProfileSerializer(profileList, many=True)
        return Response({"data": profiles.data, "message" : "Something went wrong"})


    def post(self,request):
        try:
            new_profile = ProfileSerializer(data = request.data)
            valid = new_profile.is_valid()
            if valid:
                print("************")
                new_profile.save()
                return Response({"data":new_profile.data,"message":"profile saved successfully"}, status=status.HTTP_201_CREATED )
            return Response(new_profile.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("****")
            return Response({"message" : "Somethihng went wrong"})

class TaskDetail(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    # UPDATE (PUT)
    def put(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk):
        task = self.get_object(pk)
        print("*****",task)
        if task is None:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({"message": "Task deleted"}, status=status.HTTP_200_OK)


