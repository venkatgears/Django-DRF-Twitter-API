from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Twitter_Profiles
from .serializer import Twitter_Profiles_Serializer
from django.db.models import Q
import os
import requests

# env
from dotenv import load_dotenv

load_dotenv()
# Create your views here.
TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")


@api_view(["GET"])
def endpoints(request):
    data = ["profiles/", "create_profile/:username"]
    return Response(data)


@api_view(["GET"])
def add_profile(request, username):
    head = {
        "Authorization": "Bearer " + TWITTER_API_KEY,
    }
    fields = "?user.fields=profile_image_url,username,name,description,url"
    url = "https://api.twitter.com/2/users/by/username/" + username + "/" + fields
    data = requests.get(url, headers=head).json()
    if "errors" in data:
        return Response({"error": "User not found"})
    else:
        data = data["data"]
        serializer = Twitter_Profiles_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(["GET"])
def profile_list(request):
    data = Twitter_Profiles.objects.all()
    if request.method == "GET":
        query = request.query_params.get("query")
        if query == None:
            query = ""
        elif query:
            data = Twitter_Profiles.objects.filter(
                Q(username__icontains=query) | Q(description__icontains=query)
            )
        else:
            data = Twitter_Profiles.objects.all()
        serializer = Twitter_Profiles_Serializer(data, many=True)
        return Response({"profiles": serializer.data})


@api_view(["GET", "PUT", "DELETE"])
def crud_profile(request, username):
    data = Twitter_Profiles.objects.get(username=username)
    if request.method == "GET":
        serializer = Twitter_Profiles_Serializer(data, many=False)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = Twitter_Profiles_Serializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    if request.method == "DELETE":
        data.delete()
        return Response("Entry deleted")
