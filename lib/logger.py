import logging, sys

logger = logging.getLogger('sirLogger')
stream = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("\r[%(levelname)s] %(message)s", "%H:%M:%S")
stream.setFormatter(formatter)
logger.addHandler(stream)
logger.setLevel(logging.INFO)







#Copyright RLC. IV.
#Copyright RLC. IV.
#Copyright RLC. IV.
#Copyright RLC. IV.
#Copyright RLC. IV.