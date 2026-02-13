# version 4.0.2 - 02/13/2026 - INT to BIGINT, PyMSQL to MySQLdb, mysql procedures for each server & format - see changelog
# application-level properties and references shared across app modules (files) 
from apis.properties_app import app

# Color Class used app-wide for Message Readability in console
from apis.color_class import color

# used EXIT if missing required IDs : app.importDeviceID, app.importClientID and app.importLoadID    
import sys

def add_message(message_code: int, message: str, module_name="", exceptionType="", data=None):

    # All messages handled by exceptions pass 0. message_code > 0 represent process warnings or other information to log 
    app.message_count += 1

    # Just Error handling 
    if message_code == 0:
        app.error_count += 1

    processMessage = message
    
    if exceptionType:
        processMessage = f"{exceptionType} : {message}"
        
    #if data:
    #    print(f"Exception details: {data=}, {type(data)=}")        

    if app.error_details:
        """First MySQL error does not populate warnings. This is a known issue. Just checking behavior messaging"""
        print(f"module = {color.bg.YELLOW}{color.style.BRIGHT}{module_name}{color.END} " \
              f"exceptionType = {color.bg.YELLOW}{color.style.BRIGHT}{exceptionType}{color.END} " \
              f"message = {color.bg.YELLOW}{color.style.BRIGHT}{message}{color.END} " \
              f"app.importLoadID = {color.bg.YELLOW}{color.style.BRIGHT}{app.importLoadID}{color.END} " \
              f"app.importProcessID = {color.bg.YELLOW}{color.style.BRIGHT}{app.importProcessID}{color.END}")

        # The first MySQL error does not populate warnings. This is a known issue. Just examining behavior
        showWarnings = app.dbConnection.show_warnings()
        showWarningsLen = len(showWarnings)

        if showWarningsLen == 0:
            print(f"processMessage : {processMessage}")
        else:
          print(f"Length: {color.bg.YELLOW}{showWarningsLen}{color.END} showWarnings : {color.bg.YELLOW}{showWarnings}{color.END}")

    try:
         app.cursor.callproc("messageLoad", [ processMessage, module_name, str(message_code), str(app.importLoadID), str(app.importProcessID)])
        
    except Exception as e:
        print(f"Database permissions problem : {e}")
        sys.exit(1) # Exit with error code 1
