from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Report, Source
from .serializers import ReportSerializer, ReportListSerializer, SourceSerializer, OnFlyReportSerializer


class ReportViewSet(ModelViewSet):
    """
    create:
    Return created report config.

    list:
    Return report list.

    retrieve:
    Return the given report with data.

    partial_update:
    Update the given report.

    delete:
    Delete the given report.
    """
    lookup_field = 'code'
    queryset = Report.objects.all()
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_serializer_class(self):
        if self.action in ('list', 'create', 'partial_update'):
            return ReportListSerializer

        return ReportSerializer


class SourceViewSet(ModelViewSet):
    """
    create:
    Return created source.

    list:
    Return source list.

    retrieve:
    Return the given source.

    partial_update:
    Update the given source.

    delete:
    Delete the given source.
    """
    lookup_field = 'code'
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_serializer_class(self):
        if self.action == 'report':
            return OnFlyReportSerializer

        return super().get_serializer_class()

    @action(methods=['post'], detail=True)
    def report(self, request, code):
        """ Return the given report from source by given config. """
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
