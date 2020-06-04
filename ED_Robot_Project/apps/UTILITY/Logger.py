import logging
import os


def clear_log_file_contents():
    cwd = os.getcwd()
    if "socketbot" in str(cwd).lower():
        path = str(cwd).split('SOCKETBOT')
        # make logs directory if not present.
        if not (os.path.exists(path[0] + 'SOCKETBOT\Logs')):
            os.mkdir(path[0] + 'SOCKETBOT\Logs')
        open(path[0] + 'SOCKETBOT\Logs\execution_log.log','w+').close()
    else:
        open('execution_log.log', mode='w').close()


def get_logger(name=None):

    logger = logging.getLogger('SOCKETBOT')
    if not len(logger.handlers):
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s : (%(processName)s) : %(levelname)s : %(message)s',"%Y-%m-%d %H:%M:%S")
        cwd = os.getcwd()
        if "socketbot" in str(cwd).lower():
            path = str(cwd).split('SOCKETBOT')
            file_handler = logging.FileHandler(path[0]+'SOCKETBOT\Logs\execution_log.log')
        else:
            file_handler = logging.FileHandler('execution_log.log',mode='w')

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    return logger





