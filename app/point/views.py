import xlrd
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from .serializers import PointSerializer
from .utils import save_points, catch_error


class PointsView(ModelViewSet):
    serializer_class = PointSerializer
    lookup_value_regex = '\d+'
    queryset = PointSerializer.Meta.model.objects.all()

    @catch_error(errors=(IOError, xlrd.XLRDError, ValueError),
                 rise_up=ValidationError, message={"error": "Not valid file"})
    def perform_create(self, serializer):

        file = serializer.validated_data.pop('file')
        name = file.name
        xy = save_points(file.temporary_file_path())
        points = list(xy)

        serializer.save(points=points, name=name)
