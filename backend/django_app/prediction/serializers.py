from rest_framework import serializers
from .models import Tweets

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tweets
        fields='__all__'