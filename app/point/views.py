import xlrd
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from app.point.serializers import PointSerializer
from app.point.utils import save_points


class PointsView(ModelViewSet):
    serializer_class = PointSerializer
    lookup_value_regex = '\d+'
    queryset = PointSerializer.Meta.model.objects.all()

    def perform_create(self, serializer):
        file = serializer.validated_data.pop('file')
        name = file.name
        try:
            xy = save_points(file.temporary_file_path())
            points = list(xy)
        except (IOError, xlrd.XLRDError, ValueError):
            raise ValidationError({"error": "Can't read file"})

        serializer.save(points=points, name=name)
