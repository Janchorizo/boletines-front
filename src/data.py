'''Utility functions for interacting with the database.'''
import collections

import pymysql

def create_db_wrapper(db_host, db_database, db_user, db_password):
    def caller(f, *args, **kwargs):
        keyword_args = dict(kwargs)
        keyword_args.update({
            'host': db_host,
            'database': db_database,
            'user': db_user,
            'password': db_password
        })
        return f(*args, **keyword_args)
    return caller

def execute_query(host, user, password, database, query) -> None:
    '''Execute an SQL query.'''
    
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database)

    with connection:
        with connection.cursor() as cursor:
            status = cursor.execute(query)
            if status == 0:
                r = None
            else:
                r = cursor.fetchall()

        connection.commit()
    return r

def get_date_range(host, user, password, database):
    '''Get minimum and maximum dates in the database.'''
    
    q = 'select min(date) as start, max(date) as end from boe_diary_entry;'
    start, end = execute_query(host, user, password, database, q)[0] # just one query is excuted
    return start, end


def get_entries(host, user, password, database, date):
    '''Get the title, department, cost, and links of the entries for a date.'''
    
    q = f'''select title, department, economic_impact as cost, htm_url, pdf_url
            from boe_diary_entry
            where date = '{date:%Y-%m-%d}';'''

    entries = execute_query(host, user, password, database, q)
    return entries


def get_entries_by_department_for_date(host, user, password, database, date):
    '''Get the count of entries per department and section, for a specific date.'''
    
    q = f'''select boe_diary_section.name, department, count(department) as count
            from boe_diary_entry, boe_diary_section
            where boe_diary_section.id = boe_diary_entry.section and boe_diary_entry.date = '{date:%Y-%m-%d}'
            group by department;
    '''

    data = execute_query(host, user, password, database, q)
    return data


def get_entry_types(entries):
    def get_type(entry):
        title, *_ = entry
        type_ = ''
        if title.lower().startswith('anuncio de licitación'):
            type_ = 'un anuncio de licitación'
        elif title.lower().startswith('ley'):
            type_ = 'una ley'
        elif title.lower().startswith('anuncio de formalización de contratos'):
            type_ = ' un anuncio de formalización de contratos'
        elif 'resuelve' in title.lower() and 'convocatoria' in title.lower():
            type_ = 'una resolución de convocatoria'
        elif 'convocatoria' in title.lower():
            type_ = 'una convocatoria'
        elif 'jubilación' in title.lower():
            type_ = 'una jubilación'
        elif 'cese' in title.lower():
            type_ = 'un cese'
        elif 'nombra' in title.lower():
            type_ = 'nobramiento de cargo'
        return type_

    types = collections.Counter(map(get_type, entries))
    return types

