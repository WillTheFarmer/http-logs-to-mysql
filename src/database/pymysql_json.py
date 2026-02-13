# version 4.0.2 - 02/13/2026 - INT to BIGINT, PyMSQL to MySQLdb, mysql procedures for each server & format - see changelog

# application-level properties and references shared across app modules (files) 
from apis.properties_app import app

# application-level error handle
from apis.message_app import add_message

# import pymysql
import MySQLdb

import sys

def get_connection(parms=app.mysql):
    """Establishes and returns a database connection."""
    
    mysql_host = parms.get("host")
    mysql_port = parms.get("port")
    mysql_user = parms.get("user")
    mysql_password = parms.get("password")
    mysql_schema = parms.get("schema")
    
    try:
        conn = MySQLdb.connect(host=mysql_host,
                               port=mysql_port,
                               user=mysql_user,
                               password=mysql_password,
                               database=mysql_schema,
                               connect_timeout=5,
                               local_infile=True)  

        return conn

    except MySQLdb.err.OperationalError as e:
        # DB something not found
        add_message( 0, e , __name__ , type(e).__name__ ,  e )

    except MySQLdb.err.MySQLError as e:
        # Catch specific PyMySQL errors during connection attempt
        add_message( 0, e , __name__ , type(e).__name__ ,  e )
        sys.exit(1) # Exit the script upon connection failure

    except Exception as e:
        # Catch any other potential exceptions
        add_message( 0, e , __name__ , type(e).__name__ ,  e )
        sys.exit(1)
