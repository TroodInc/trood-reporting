from trood_reporting.adapters import psql

def test_psql_build_query():
    """ Test PostgreSQL query builder. """
    query = 'SELECT {% if value %}({{ value }}){% else %}(1){% endif %};'
    recivied_query, _ = psql.build_query(query, {'value': 0})
    expected_query = 'SELECT (1);'
    assert recivied_query == expected_query
    recivied_query, _ = psql.build_query(query, {'value': 2})
    expected_query = 'SELECT (%(value)s);'
    assert recivied_query == expected_query
