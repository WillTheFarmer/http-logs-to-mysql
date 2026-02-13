/* 10 Store Procedures process http Access & Error Log LOAD DATA tables. LOAD DATA tables contain raw log data.

Each Stored Procedure has 2 parameters. First is Access & Error LogFormats. Second parameter is importLoadID and important for processing.
- IN in_processName VARCHAR(100) - LogFormat to process. 
NOTE: For normalize_useragent parameter can be any string >= 8 characters. It is for reference use only
- IN in_importLoadID VARCHAR(20) - importLoadID to process. Valid values 'ALL' or a value converted to INTEGER=importLoadID   
NOTE: if in_importLoadID='ALL' ONLY importLoadID records with import_load TABLE "completed" COLUMN NOT NULL will be processed.
This avoids interfering with Python client modules uploading files at same time as server STORED PROCEDURES executing.
 
LOAD DATA stage tables - load_access_combined, load_access_csv2mysql, load_access_vhost, load_access_nginx_default, load_error_apache, load_error_nginx have a process_status COLUMN.
process_status=0 - LOAD DATA tables loaded with raw log data
process_status=1 - process_error_parse or process_access_parse executed on record
process_status=2 - process_error_import or process_access_import executed on record

import_file TABLE - record for every Access & Error file processed by Python processFiles. LOAD DATA tables have FOREIGN KEY (importfileid).
import_load TABLE - record for every execution of Python process. Each record contains information on LogFormat log files processed. 
import_load TABLE "completed" COLUMN - is NULL an error occurred. Refer to the import_error TABLE for error details.
import_process TABLE - record for every import process execution. IF IMPORT LOAD = importloadid is NOT NULL, If STORED PROCEDURE = importserverid is NOT NULL.
import_process TABLE "completed" COLUMN - is NULL an error occurred. Refer to the import_error TABLE for error details.
import_error TABLE - only table using ENGINE=MYISAM due to disregarding TRANSACTION ROLLBACK. Any errors in Python or MySQL recorded in table. 

CALL Commands execute each Stored Procedure for each Import Format. 'ALL' processes any unprocessed importLoadID(s) based on process_status. 
NOTE: Each Python 'processLogs' function execution creates a new importLoadID. Every execution has a unique importLoadID value & record.
*/
USE http_logs;
# Apache error logs
CALL parse_error_apache('default','ALL'); 
CALL import_error_apache('default','ALL'); 

# Apache access logs - Combined and Common format
CALL parse_access_apache('combined','ALL'); 
CALL import_access_apache('combined','ALL'); 

# Apache access logs - Vhost format
CALL parse_access_apache('vhost','ALL'); 
CALL import_access_apache('vhost','ALL'); 

# Apache access logs - Comma Separated Values format
CALL parse_access_apache('csv2mysql','ALL'); 
CALL import_access_apache('csv2mysql','ALL'); 

# NGINX error logs - Default Combined format
CALL parse_error_nginx('default','ALL'); 
CALL import_error_nginx('default','ALL'); 

# NGINX access logs - Default Combined format
CALL parse_access_nginx('combined','ALL'); 
CALL import_access_nginx('combined','ALL'); 

# Parses and normalization Data found in User-Agent string
CALL normalize_useragent('Any Process Name','ALL');

# Retreives GeoIP Data about the remote client IP address
CALL normalize_client('Any Process Name','ALL');



