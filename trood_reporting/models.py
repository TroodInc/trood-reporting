import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


def default_uuid():
    return uuid.uuid4().hex


class BaseModel(models.Model):
    """ Base Trood Reporting model. """
    code = models.CharField(
        default=default_uuid, max_length=128,
        unique=True, db_index=True, help_text=_('Code')
    )
    title = models.CharField(
        max_length=128, help_text=_('Title'), blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True, help_text=_('Created'))
    edited = models.DateTimeField(auto_now=True, help_text=_('Created'))
    deleted = models.DateTimeField(blank=True, null=True, help_text=_('Deleted'))
    # TODO:
    # creator
    # editor

    class Meta:
        abstract = True


class Source(BaseModel):
    """ Data source connection settings. """
    class Type:
        postgres = 'PSQL'
        druid = 'DRUID'

        choices = (
            (postgres, _('PostgreSQL')),
            (druid, _('Druid'))
        )

    type = models.CharField(
        max_length=16, choices=Type.choices, help_text=_('Source type')
    )
    dsn = models.CharField(
        max_length=1024, help_text=_('Source connection string')
    )

    def __str__(self):
        return self.dsn


class Report(BaseModel):
    """ Report settings. """
    source = models.ForeignKey(
        Source, on_delete=models.CASCADE, help_text=_('Report source')
    )
    query = models.TextField(help_text=_('Query string'))

    def __str__(self):
        return self.code
