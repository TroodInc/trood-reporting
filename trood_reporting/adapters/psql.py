import psycopg2
from jinjasql import JinjaSql


LOOKUPS = {
    'gte': '>=',
    'gt': '>',
    'lte': '<=',
    'lt': '<',
}


def build_query(query, query_args):
    jinja = JinjaSql(param_style='pyformat')
    query, bind_params = jinja.prepare_query(query, query_args)
    return query, bind_params


def retrive_report(query, query_args, source):
    # TODO: implement try/except
    query, bind_params = build_query(query, query_args)
    connection = psycopg2.connect(source.dsn)
    cursor = connection.cursor()
    cursor.execute(query, bind_params)
    data = cursor.fetchall()
    columns = [c.name for c in cursor.description]
    cursor.close()
    connection.close()
    return [dict(zip(columns, d)) for d in data]
