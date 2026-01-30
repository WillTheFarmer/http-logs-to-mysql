# version 4.0.1 - 01/24/2026 - Proper Python code, NGINX format support and Python/SQL repository separation - see changelog
#
# function: copy_backup_file
# synopsis: if file already been imported but still found in a GLOB directory search repeatedly.
# Based on settings this option can remove it.
# author: Will Raymond <farmfreshsoftware@gmail.com>

# for relpath, join and dirname functions
from os import path

# used to handle copying files
import shutil

# used to make directory structure same as current file location.
from os import makedirs

# safe file delete
from os import remove

# application-level properties and references shared across app modules (files) 
from apis.properties_app import app

# application-level error handle
from apis.message_app import add_message

# Color Class used app-wide for Message Readability in console
from apis.color_class import color
    
def copy_backup_file(log_path_file, log_days):
    
    fileCopied = False

    if app.backup_days > 0 and log_days > app.backup_days:

        log_relpath = path.relpath(log_path_file, app.watch_path)

        copy_path =  path.join(app.backup_path, log_relpath)

        try:
            makedirs(path.dirname(copy_path), exist_ok=True)
       
            try:
                shutil.copy2(log_path_file, copy_path)
                print(f"{color.fg.GREEN}{color.style.NORMAL}Copied file to : {copy_path}{color.END}")
                fileCopied = True

            except FileNotFoundError as e:
                add_message( 0, {e}, {__name__}, {type(e).__name__},  e)

            except PermissionError as e:
                add_message( 0, {e}, {__name__}, {type(e).__name__},  e)

            except shutil.SameFileError as e:
                add_message( 0, {e}, {__name__}, {type(e).__name__},  e)

            except OSError as e:
                add_message( 0, {e}, {__name__}, {type(e).__name__},  e)

        except FileExistsError as e:
            add_message( 0, {e}, {__name__}, {type(e).__name__},  e)

        except PermissionError as e: 
            add_message( 0, {e}, {__name__}, {type(e).__name__},  e)

        except Exception as e:
            add_message( 0, {e}, {__name__}, {type(e).__name__},  e)

    if app.backup_days == -1 or fileCopied:
        try:
            remove(log_path_file)
            print(f"{color.bg.CYAN}{color.style.BRIGHT}Deleted file : {log_path_file}{color.END}")

        except Exception as e:
            add_message( 0, {e}, {__name__}, {type(e).__name__},  e)
              
def update_value(current_value):
    # Do some operations
    current_value += 1
    return current_value
