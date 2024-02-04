from rest_framework import serializers
from .models import UserAttribute, UserSegment, UserAttributeFilter, UserFilterCondition, ActivityFilter

class UserAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAttribute
        fields = '__all__'

class UserSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSegment
        fields = '__all__'

class UserAttributeFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAttributeFilter
        fields = '__all__'

class UserFilterConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFilterCondition
        fields = '__all__'

class ActivityFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityFilter
        fields = '__all__'