# version 4.0.2 - 02/13/2026 - INT to BIGINT, PyMSQL to MySQLdb, mysql procedures for each server & format - see changelog
from tabulate import tabulate
# Message Readability in console
from apis.color_class import color
# all starts is here - json process file must exist
from config.config_app import load_file
config = load_file()

if config:
# Four Python modules are passed different parameters to import different log formats
    process_list = []

    print(f"{color.fg.GREEN}Process List{color.fg.YELLOW} - Each record is different parameters passed to 1 of 4 Python Modules - {color.fg.RED}(Module Name){color.END}")
    for process in config['processes']:
#        print(f"Process ID: {process.get("id")}. module_name: {process.get("module_name")}")
        attrValues = {}
        processInfo = {"Status": process.get("status"),
                       "Process id": process.get("id"),
                       "Process Group": process.get("group"),
                       "Process Name": process.get("name"),
                       "Module Name": process.get("module_name")}

        attributes = process.get("attributes")
        if process.get("module_name") == "data_file_loader":
           attrValues = {"Parameter": attributes["path"]} 
#           attrValues = {"Path": attributes["path"],"Recursive": attributes["recursive"]} 
        elif process.get("module_name") == "database_module":
           attrValues = {"Parameter": attributes["module_name"] + " - " + attributes["module_parm1"]} 
#           attrValues = {"Module": attributes["module_name"],"Parameter": attributes["module_parm1"]} 
        
        processInfo.update(attrValues)
        process_list.append(processInfo)

    print(tabulate(process_list, headers='keys', tablefmt='github'))

# Create any number of observers. Each log format will require a separate observer to associate proper import processes. Execute a single LOAD process. Other processes executed somewhere else.
    observer_list = []
    print(f"{color.fg.GREEN}Observer List{color.fg.YELLOW} - Each record is a watchDog Observer Schedule. Each Observer executes associated import processes - {color.fg.RED}(process_list){color.END}")
    for observer in config['observers']:
        observerInfo = {"Status": observer.get("status"),
                        "id": observer.get("id"),
                        "name": observer.get("name"),
                        "path": observer.get("path"),
                        "recursive": observer.get("recursive"),
                        "interval":  observer.get("interval"),
                        "process_list": observer.get("process_list")}

        observer_list.append(observerInfo)

    print(tabulate(observer_list, headers='keys', tablefmt='github'))
