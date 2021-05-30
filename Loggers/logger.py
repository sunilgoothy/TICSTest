import logging
import sys

#Setup logger
Log = logging.getLogger('mylogger')
Log.addHandler(logging.FileHandler('logger.log'))
Log.addHandler(logging.StreamHandler(sys.stdout))
Log.setLevel('DEBUG')


print("Starting Program.....")
Log.info("Info Logging....")
Log.warning("WARNING Logging....")
Log.debug("DEBUG Logging....")
Log.error("ERROR Logging....")
Log.critical("CRITICAL Logging....")

    
try:
    b = 1 / 0
except Exception as e:
    Log.error(f"Exception log as Error: {e}")

try:
    a = 1 / 0
except Exception as e:
    Log.exception(f"Exception log as exception with traceback: {e}")
