from util.db.sql_table import SqlTable

def get_table(schema):
    return SqlTable(schema, {
                "dialect": "postgresql",
                "driver": "psycopg2",
                "username": "posgres",
                "password": "123",
                "host": "localhost",
                "port": 5432,
                "database": "educat"
            })