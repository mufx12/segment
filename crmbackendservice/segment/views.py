
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView

from .models import Event, DataType, Country,UserAttribute, UserSegment, UserAttributeFilter, UserFilterCondition, ActivityFilter
from .serializers import UserAttributeSerializer, UserSegmentSerializer, UserAttributeFilterSerializer, UserFilterConditionSerializer, ActivityFilterSerializer

class UserAttributeViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset =UserAttribute.objects.all()
        serializer = UserAttributeSerializer(queryset, many=True)
        return Response(serializer.data)




class UserSegmentViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = UserSegment.objects.all()
        serializer = UserSegmentSerializer(queryset, many=True)
        return Response(serializer.data)



class UserAttributeFilterViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = UserAttributeFilter.objects.all()
        serializer = UserAttributeFilterSerializer(queryset, many=True)
        return Response(serializer.data)

class UserFilterConditionViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = UserFilterCondition.objects.all()
        serializer = UserFilterConditionSerializer(queryset, many=True)
        return Response(serializer.data)

class ActivityFilterViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = ActivityFilter.objects.all()
        serializer = ActivityFilterSerializer(queryset, many=True)
        return Response(serializer.data)

