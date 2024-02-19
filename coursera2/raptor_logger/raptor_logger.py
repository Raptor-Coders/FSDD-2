import logging

#  Configure the logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('student_model')

#  Log messages at different levels
# logger.debug('Debug message')
# logger.info('Informational message')
# logger.warning('warning message')
# logger.error('Error message')
logger.critical('Critical error')