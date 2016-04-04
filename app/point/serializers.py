from django.conf import settings
from rest_framework import serializers

from app.point.models import PointSet


class PointSerializer(serializers.ModelSerializer):
    file = serializers.FileField(max_length=255, allow_empty_file=False, write_only=True)

    class Meta:
        model = PointSet
        fields = ('id','name', 'points', 'date', 'file')
        extra_kwargs = {
            'points': {'read_only': True},
            'name': {'read_only': True}
        }

    def create(self, validated_data):
        return super(PointSerializer, self).create(validated_data)

    def validate_file(self, value):
        if value.content_type in settings.ALLOWED_EXCEL.values():
            return value
        raise serializers.ValidationError('Not allowed type for file')
