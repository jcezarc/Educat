import os
from util.db.lite_table import LiteTable

# ----------------------------------------------
EDUCAT_USER = os.environ.get(
    'EDUCAT_USER',
    '<<** Coloque aqui seu usuário **>>'
)
EDUCAT_PASSWORD = os.environ.get(
    'EDUCAT_PASSWORD',
    '<<** Coloque aqui sua senha **>>'
)
EDUCAT_HOST = os.environ.get(
    'EDUCAT_HOST',
    'localhost'
)
# ----------------------------------------------

def get_table(schema):
    return LiteTable(schema, {
        # ---- MySql -------------------------
            # "host": EDUCAT_HOST,
            # "user": EDUCAT_USER,
            # "password": EDUCAT_PASSWORD,
            # "database": "educat"
        # ---- Sqlite -----------------------
                    "database": "educat.db"
        })
