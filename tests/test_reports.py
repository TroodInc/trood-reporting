from django.urls import reverse


def test_create_source(client, headers, source_conf):
    """ Test create report source. """
    response = client.post(reverse('v1:source-list'), source_conf, **headers)
    assert response.status_code == 201


def test_retrive_source(client, headers, source):
    """ Test retrive report source. """
    response = client.get(
        reverse('v1:source-detail', kwargs={'code': source.code}), **headers
    )
    assert response.status_code == 200


def test_update_source(client, headers, source):
    """ Test update report source. """
    response = client.patch(
        reverse('v1:source-detail', kwargs={'code': source.code}),
        {'code': 'XXX'},
        **headers
    )
    assert response.status_code == 200


def test_delete_source(client, headers, source):
    """ Test delete report source. """
    response = client.delete(
        reverse('v1:source-detail', kwargs={'code': source.code}),
        **headers
    )
    assert response.status_code == 204


def test_create_report(client, headers, report_conf):
    """ Test create report. """
    report_conf['source'] = report_conf['source'].code
    response = client.post(
        reverse('v1:report-list'), report_conf, **headers
    )
    assert response.status_code == 201


def test_retrive_report(client, headers, report):
    """ Test retrive report with data. """
    response = client.get(
        reverse('v1:report-detail', kwargs={'code': report.code}), **headers
    )
    assert response.status_code == 200


def test_update_report(client, headers, report):
    """ Test update report with data. """
    response = client.patch(
        reverse('v1:report-detail', kwargs={'code': report.code}),
        {'title': 'Test'},
        **headers
    )
    assert response.status_code == 200


def test_delete_report(client, headers, report):
    """ Test delete report with data. """
    response = client.delete(
        reverse('v1:report-detail', kwargs={'code': report.code}), **headers
    )
    assert response.status_code == 204


def test_retrive_report_by_conf(client, headers, source, on_fly_report_conf):
    """ Test retrive report by config. """
    response = client.post(
        reverse('v1:source-report', kwargs={'code': source.code}),
        on_fly_report_conf,
        **headers
    )
    assert response.status_code == 200
