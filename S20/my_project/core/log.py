import logging
from conf.settings import log_path,level

class Log(object):
    if hasattr(logging,level.upper()):
        level = getattr(logging,level.upper())
    else:
        level = logging.DEBUG
    def __init__(self, level=level):
        logger = logging.getLogger()
        logger.setLevel(level)
        fh = logging.FileHandler(log_path, encoding='utf-8')
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        self.logger = logger

log = Log()