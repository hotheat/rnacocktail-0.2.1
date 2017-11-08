import logging
import os
import time

logger = logging.getLogger(__name__)


def create_dirs(dirlist):
    for dirname in dirlist:
        if not os.path.isdir(dirname):
            logger.info("Creating directory %s" % (dirname))
            try:
                os.makedirs(dirname)
            except Exception as e:
                return True

