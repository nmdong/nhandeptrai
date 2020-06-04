# This file will be used to write python functions that can be
# used as extensions in robot files.
from UTILITY import Logger


logger = Logger.get_logger(__name__)



def log_to_execution_log_file(line,level=None):
    if str(level).lower() == 'info':
        logger.info(line)
    elif str(level).lower() == 'warn':
        logger.warning(line)
    elif str(level).lower() == 'error':
        logger.error(line)
    else:
        logger.debug(line)






