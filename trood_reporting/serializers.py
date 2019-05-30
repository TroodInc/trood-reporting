from rest_framework.serializers import ModelSerializer, SerializerMethodField, SlugRelatedField, CharField, JSONField, ChoiceField

from .models import Report, Source
from .adapters.psql import retrive_report


class SourceSerializer(ModelSerializer):

    type = ChoiceField(choices=Source.Type.choices, help_text='Druid not implemented!!!')

    class Meta:
        model = Source
        fields = ('code', 'title', 'type', 'dsn')


class ReportListSerializer(ModelSerializer):

    source = SlugRelatedField(slug_field='code', queryset=Source.objects.all())

    class Meta:
        model = Report
        fields = ('source', 'code', 'query')


class ReportSerializer(ModelSerializer):
    data = SerializerMethodField(help_text='Data from source. JSON.')

    class Meta:
        model = Report
        fields = ('code', 'data')

    def get_data(self, obj):
        return retrive_report(
            obj.query, self.context['request'].query_params, obj.source
        )


class OnFlyReportSerializer(ModelSerializer):
    data = SerializerMethodField(help_text='Data from source. JSON.')
    query = CharField(help_text='Report query.')
    query_params = JSONField(help_text='Query filter parameters.', required=False, default={})

    class Meta:
        model = Source
        fields = ('data', 'query', 'query_params')

    def get_data(self, obj):
        query = self.validated_data['query']
        query_params = self.validated_data['query_params']
        return retrive_report(query, query_params, obj)

    def to_representation(self, instance):
        instance.query = self.validated_data['query']
        instance.query_params = self.validated_data['query_params']
        return super().to_representation(instance)
