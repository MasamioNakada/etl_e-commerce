import mysql_db as mysql

from os import environ

user_mysql = environ.get("user_mysql")
pass_mysql = environ.get("pass_mysql")
host = "localhost"

db_name = "ecommerce"


def load_to_database(labels):
    # crear la conexion
    engine = mysql.create_db_connection(host, user_mysql, pass_mysql)

    # crear la base de datos
    mysql.create_database(engine, f"CREATE DATABASE IF NOT EXISTS {db_name}")
    mysql.execute_query(engine, "USE ecommerce")

    # crear la concexion a la base de datos:
    engine = mysql.create_db_connection(host, user_mysql, pass_mysql, db_name)

    # crear las tabla maestra:

    localidades_query = "CREATE TABLE IF NOT EXISTS Localidades(categoria VARCHAR(255),centroide_lat FLOAT(8),centroide_lon FLOAT(8), departamento_nombre  "
    localidades_query = """
    CREATE TABLE IF NOT EXISTS
    """

    mysql.execute_query(
        engine,
    )
