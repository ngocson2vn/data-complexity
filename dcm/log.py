import os
import logging
import dcm

MSG_FORMAT = '%(asctime)s %(levelname)s %(name)s: %(message)s'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(format=MSG_FORMAT, datefmt=DATETIME_FORMAT, level=logging.INFO)

def getLogger():
  logLevel = logging.DEBUG if dcm.__DEBUG__ else logging.INFO
  logger = logging.getLogger('dcm')
  logger.setLevel(logLevel)
  return logger
