'''Utility functions for interacting with the database.'''
import collections

import pymysql
import pymongo
from pymongo import MongoClient

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

def get_date_range(dburi, dbname):
    '''Get minimum and maximum dates in the database.'''
    
    collection = 'diary_summary'
    client = MongoClient(dburi)
    db = client[dbname]
    cursor = db[collection].aggregate([
        {'$group': {'_id': '', 'max': {'$max': '$date'}, 'min': {'$min': '$date'}}}
    ])
    
    date_range = next(cursor)
    client.close()

    first_date = datetime.datetime(*map(int, date_range['min'].split('-')))
    last_date = datetime.datetime(*map(int, date_range['max'].split('-')))

    return first_date, last_date

def get_diary_summary(dburi, dbname, date):
    '''Get minimum and maximum dates in the database.'''
    
    collection = 'diary_summary'
    client = MongoClient(dburi)
    db = client[dbname]
    cursor = db[collection].findOne({'date': f'{date:%Y-%m-%d}'})
    
    data = next(cursor)
    client.close()

    return data

def get_viz_data(dburi, dbname, date):
    '''Get minimum and maximum dates in the database.'''
    
    collection = 'dash_data'
    client = MongoClient(dburi)
    db = client[dbname]
    cursor = db[collection].findOne({'date': f'{date:%Y-%m-%d}'})
    
    data = next(cursor)
    client.close()

    return data

def get_entries(host, user, password, database, date):
    '''Get the title, department, cost, and links of the entries for a date.'''
    
    q = f'''select title, section, department, economic_impact as cost, htm_url, pdf_url
            from boe_diary_entry
            where date = '{date:%Y-%m-%d}';'''

    entries = execute_query(host, user, password, database, q)
    return entries
