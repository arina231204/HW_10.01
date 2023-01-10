from django.shortcuts import render
from rest_framework import viewsets, mixins, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ProfileRegisteSerializers
from .models import Profile,User

class ProfileRegisterAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisteSerializers

    def create_profile(self,request, is_author):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save(is_author=is_author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def author(self, request, pk=None):
        return self.create_profile(request, True)

    @action(methods=['POST'], detail=False)
    def guest(self, request, pk=None):
        return self.create_profile(request, False)

