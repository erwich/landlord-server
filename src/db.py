from mysql.connector import (
    connection
)

from config import config

landlord = connection.MySQLConnection(
    user=config["database"]["user"],
    password=config["database"]["password"],
    host=config["database"]["host"],
    port=config["database"]["port"],
    database=config["database"]["database"]
)

def execute_query(sql, database, params, use_dict=True):
    cursor = database.cursor(dictionary=use_dict)
    cursor.execute(
        sql,
        params
    )
    print(sql)
    print(params)
    return cursor.fetchall()