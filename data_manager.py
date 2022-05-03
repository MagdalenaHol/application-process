from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor, last_name):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE lower(last_name) = lower(%(last_name)s)
        ORDER BY first_name"""
    l_name = {'last_name': last_name}
    cursor.execute(query, l_name)
    return cursor.fetchall()


@database_common.connection_handler
def get_city_name(cursor, city):
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city = (%(city)s)"""
    city_ = {'city': city}
    cursor.execute(query, city_)
    return cursor.fetchall()


@database_common.connection_handler
def get_applicant_data_by_name(cursor, name):
    query = """
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE lower(first_name) = lower(%(name)s)"""
    applicant_ = {'name': name}

    cursor.execute(query, applicant_)
    return cursor.fetchall()
