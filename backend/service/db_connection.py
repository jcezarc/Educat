import os
from util.db.dynamo_table import DynamoTable
from util.db.sql_table import SqlTable
from util.db.mongo_table import MongoTable
from util.db.neo4j_table import Neo4Table
from util.db.lite_table import LiteTable

# ----------------------------------------------
EDUCAT_DB_TYPE = os.environ.get(
    'EDUCAT_DB_TYPE',
        # <** Escolha um dos tipos de BD **>
        # - MySql
        # - Postgres
        # - MongoDB
        # - SqlServer
        # - DynamoDB
        # - Neo4J
        # - Sqlite
    'Postgres'
)
EDUCAT_USER = os.environ.get(
    'EDUCAT_USER',
    'postgres'
)
EDUCAT_PASSWORD = os.environ.get(
    'EDUCAT_PASSWORD',
    'jucabala'
)
EDUCAT_HOST = os.environ.get(
    'EDUCAT_HOST',
    'localhost'
)
# ----------------------------------------------

def get_table(schema):
    db_types = {
        'DynamoDB': lambda: DynamoTable(schema, {
            "service_name": "dynamodb",
            "region_name": "us-west-2",
            "endpoint_url": f"http://{EDUCAT_HOST}:8000",
            "aws_access_key_id": EDUCAT_USER,
            "aws_secret_access_key": EDUCAT_PASSWORD,
        }),
        'SqlServer': lambda: SqlTable(schema, {
            "dialect": "mssql",
            "driver": "pyodbc",
            "username": EDUCAT_USER,
            "password": EDUCAT_PASSWORD,
            "host": EDUCAT_HOST,
            "port": 1433,
            "database": "inquest"
        }),
        'MongoDB': lambda: MongoTable(schema, {
            # "server": "mongodb+srv://",
            "server": "",
            "host_or_user": EDUCAT_USER,
            "port_or_password": EDUCAT_PASSWORD,
            "database": "inquest"
        }),
        'Postgres': lambda: SqlTable(schema, {
            "dialect": "postgresql",
            "driver": "psycopg2",
            "username": EDUCAT_USER,
            "password": EDUCAT_PASSWORD,
            "host": EDUCAT_HOST,
            "port": 5432,
            "database": "inquest"
        }),
        'Neo4J': lambda: Neo4Table(schema, {
            "host": EDUCAT_HOST,
            "port": 7687,
            "user": EDUCAT_USER,
            "password": EDUCAT_PASSWORD
        }),
        'Sqlite': lambda: LiteTable(schema, {
            "timeout": 5,
            "cached_statements": 100,
            "uri": True,
            "check_same_thread": True
        }),
        'MySql': lambda: LiteTable(schema, {
            "host": EDUCAT_HOST,
            "user": EDUCAT_USER,
            "password": EDUCAT_PASSWORD,
            "database": "inquest"
        }),
    }
    func = db_types[EDUCAT_DB_TYPE]
    return func()
