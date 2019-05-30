import json

import pytest
from django.core import management
from django.urls import reverse

from trood_reporting.models import Source, Report


def pytest_configure(config):
    config.DEBUG = True


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope='function')
def headers():
    """ Headers for API calls. """
    yield {
        'Authorization': 'Token TEST_TOKEN',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
    }


@pytest.fixture(scope='function')
def source_conf():
    """ Test source config data. """
    yield {
        'type': Source.Type.postgres,
        'dsn': 'postgres://custodian:custodian@127.0.0.1:5432/custodian'
    }


@pytest.fixture(scope='function')
def source(source_conf):
    """ Test data source. """
    yield Source.objects.create(**source_conf)


@pytest.fixture(scope='function')
def report_conf(source):
    """ Test report conf. """
    yield {
        'code': 'test-report', 'source': source, 'query': 'SELECT (1);'
    }


@pytest.fixture(scope='function')
def report(report_conf):
    """ Test report. """
    yield Report.objects.create(**report_conf)


@pytest.fixture(scope='function')
def on_fly_report_conf(source):
    """ Test on fly report conf. """
    yield {'query': 'SELECT (1);', 'query_params': {}}
