# LOGGING Levels
# https://docs.python.org/3/howto/logging.html#logging-levels

import logging
import sys

#Setup logger
Log = logging.getLogger('mylogger')
Log.addHandler(logging.FileHandler('logger.log'))
Log.addHandler(logging.StreamHandler(sys.stdout))
Log.setLevel('DEBUG')

def get_debug_level():
    CURRENT_LEVEL = logging.getLevelName(Log.getEffectiveLevel())
    print(f"Current Debug Level: {CURRENT_LEVEL}")
    return CURRENT_LEVEL

print("Starting Program.....")
Log.info("Info Logging....")
Log.warning("WARNING Logging....")
Log.debug("DEBUG Logging....")
Log.error("ERROR Logging....")
Log.critical("CRITICAL Logging....")

def test_func():
    print("This statement is printed inside test_func")
    
try:
    b = 1 / 0
except Exception as e:
    Log.error(f"Exception log as Error: {e}")

try:
    a = 1 / 0
except Exception as e:
    Log.exception(f"Exception log as exception with traceback: {e}")

# get debug level
print(get_debug_level())


Log.setLevel('DEBUG')
# Execute only if matches debug level
if get_debug_level() == 'DEBUG':
    Log.debug(test_func())

