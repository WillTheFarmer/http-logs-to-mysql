CREATE USER 'http_upload'@'localhost' IDENTIFIED BY 'Just4TheData';
-- Python module CALLS Stored Procedures for log processing & Stored Procedure for error logging
GRANT EXECUTE ON PROCEDURE parse_access_apache TO `http_upload`@`localhost`;
GRANT EXECUTE ON PROCEDURE import_access_apache TO `http_upload`@`localhost`;
GRANT EXECUTE ON PROCEDURE parse_error_apache TO `http_upload`@`localhost`;
GRANT EXECUTE ON PROCEDURE import_error_apache TO `http_upload`@`localhost`;
GRANT EXECUTE ON PROCEDURE parse_access_nginx TO `http_upload`@`localhost`;
GRANT EXECUTE ON PROCEDURE import_access_nginx TO `http_upload`@`localhost`;
GRANT EXECUTE ON PROCEDURE parse_error_nginx TO `http_upload`@`localhost`;
GRANT EXECUTE ON PROCEDURE import_error_nginx TO `http_upload`@`localhost`;
GRANT EXECUTE ON PROCEDURE normalize_useragent TO `http_upload`@`localhost`;
GRANT EXECUTE ON PROCEDURE normalize_client TO `http_upload`@`localhost`;
-- Python module CALLS Stored Procedures for error logging
GRANT EXECUTE ON PROCEDURE messageLoad TO `http_upload`@`localhost`;
-- Python module SELECTS Stored Functions for log processing
GRANT EXECUTE ON FUNCTION importDeviceID TO `http_upload`@`localhost`;
GRANT EXECUTE ON FUNCTION importClientID TO `http_upload`@`localhost`;
GRANT EXECUTE ON FUNCTION importLoadID TO `http_upload`@`localhost`;
GRANT EXECUTE ON FUNCTION importLoadProcessID TO `http_upload`@`localhost`;
GRANT EXECUTE ON FUNCTION importFileExists TO `http_upload`@`localhost`;
GRANT EXECUTE ON FUNCTION importFileID TO `http_upload`@`localhost`;
-- Python module INSERTS into TABLES executing LOAD DATA LOCAL INFILE for log processing
GRANT INSERT ON load_access_combined TO `http_upload`@`localhost`;
GRANT INSERT ON load_access_csv TO `http_upload`@`localhost`;
GRANT INSERT ON load_access_vhost TO `http_upload`@`localhost`;
GRANT INSERT ON load_access_nginx TO `http_upload`@`localhost`;
GRANT INSERT ON load_error_apache TO `http_upload`@`localhost`;
GRANT INSERT ON load_error_nginx TO `http_upload`@`localhost`;
-- Python module issues SELECT and UPDATE statements on TABLES due to converting parameters.
-- Only reason TABLE direct access is number of parameters required for Stored Procedure.
GRANT SELECT,UPDATE ON access_log_useragent TO `http_upload`@`localhost`;
GRANT SELECT,UPDATE ON import_load TO `http_upload`@`localhost`;
GRANT SELECT,UPDATE ON log_client TO `http_upload`@`localhost`;
