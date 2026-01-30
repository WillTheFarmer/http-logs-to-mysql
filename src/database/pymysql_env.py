# version 4.0.1 - 01/24/2026 - Proper Python code, NGINX format support and Python/SQL repository separation - see changelog

# application-level error handle
from apis.message_app import add_message

import pymysql
import sys

from os import getenv
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

mysql_host = getenv('MYSQL_HOST')
mysql_port = int(getenv('MYSQL_PORT'))
mysql_user = getenv('MYSQL_USER')
mysql_password = getenv('MYSQL_PASSWORD')
mysql_schema = getenv('MYSQL_SCHEMA')

def get_connection():
    try:
        conn = pymysql.connect(host=mysql_host,
                               port=mysql_port,
                               user=mysql_user,
                               password=mysql_password,
                               database=mysql_schema,
                               connect_timeout=5,
                               local_infile=True)  

        return conn

    except pymysql.err.OperationalError as e:
        # DB something not found
        add_message( 0, {e}, {__name__}, {type(e).__name__},  e )

    except pymysql.err.MySQLError as e:
        # Catch specific PyMySQL errors during connection attempt
        add_message( 0, {e}, {__name__}, {type(e).__name__},  e )
        sys.exit(1) # Exit the script upon connection failure

    except Exception as e:
        # Catch any other potential exceptions
        add_message( 0, {e}, {__name__}, {type(e).__name__},  e )
        sys.exit(1)
