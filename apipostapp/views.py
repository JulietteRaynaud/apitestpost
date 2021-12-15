from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from apipostapp.models import Post
from apipostapp.serializers import postSerialisers
# Create your views here.

@csrf_exempt
def postApi(request, id=0):
    if request.method=='GET':
        post = Post.objects.all()
        post_serializer = postSerialisers(post,many=True)
        return JsonResponse(post_serializer.data, safe=False)
    elif request.method=='POST':
        post_data=JSONParser().parse(request)
        post_serializer= postSerialisers(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("added succesfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        post_data=JSONParser().parse(request)
        post=Post.objects.get(postId=post_data['postId'])
        post_serialiser = postSerialisers(post, data=post_data)
        if post_serialiser.is_valid():
            post_serialiser.save()
            return JsonResponse("update sucessfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        post = Post.objects.get(postId=id)
        post.delete()
        return JsonResponse("Delete successfully", safe=False)