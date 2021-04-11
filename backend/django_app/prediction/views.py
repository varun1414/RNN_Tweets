from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.views import APIView
from prediction.apps import PredictionConfig
from . models import Tweets
from . serializers import TweetSerializer

# Create your views here.
# Class based view to predict based on IRIS model
class Tweet_List(APIView):
    def post(self, request, format=None):
        
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,format=None):
        tweet = Tweets.objects.all()
        tweet = TweetSerializer(tweet,many=True) 
        return JsonResponse(tweet.data,safe=False) 
