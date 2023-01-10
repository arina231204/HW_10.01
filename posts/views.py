from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly, IsNotAuthorPermission
from .models import Tweet, StatusTweet, Comment, Like
from rest_framework import generics

from .serializers import TweetSerializer, StatusTweetSerializer, CommentSerializer, LikeSerializer


class TweetViewSet(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)




class CommentViewSet(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)




class TweetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class SecondTweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    # permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    @action(methods=['POST'], detail=True)
    def leave_status(self, request, pk=None):
        serializer = StatusTweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                tweet=self.get_object(),
                profile=request.user.profile
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['post'])
    # def like(self, request, pk=None):
    #     tweet = self.get_object()
    #     profile = request.user
    #
    #     if tweet.has_like_from_user(profile):
    #         like = tweet.like_set.get(profile=profile)
    #         like.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #
    #     like = Like.objects.create(profile=profile, tweet=tweet)
    #     serializer = LikeSerializer(like)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class SecondCommentViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    @action(methods=['POST'], detail=True)
    def leave_status(self, request, pk=None):
        serializer = StatusTweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                tweet=self.get_object(),
                profile=request.user.profile
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeTweetView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=kwargs.get('tweet_id'))
        profile = request.profile
        if tweet.likes.filter(pk=profile.pk).exists():
            tweet.likes.remove(profile)
        else:
            tweet.likes.add(profile)
        return redirect('tweet_detail', tweet_id=tweet.pk)