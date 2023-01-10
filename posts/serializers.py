from rest_framework import serializers

from .models import Tweet, Comment, StatusTweet, StatusComment, Like


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
        read_only_fields = ['profile']

class StatusTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTweet
        fields = '__all__'
        read_only_fields = ['profile','tweet' ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['profile']

class StatusCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusComment
        fields = '__all__'
        read_only_fields = ['profile','tweet' ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'profile', 'tweet')
        read_only_fields = ('id', 'profile', 'tweet')