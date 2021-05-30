# Reference https://github.com/Delgan/loguru#readme
from loguru import logger

# Only console messages
logger.info("Info Logging....")
logger.warning("WARNING Logging....")
logger.debug("DEBUG Logging....")
logger.error("ERROR Logging....")
logger.critical("CRITICAL Logging....")

# Add filehandler
logger.add("log_{time}.log")

logger.info("Info Logging in file....")
logger.warning("WARNING Logging in file....")
logger.debug("DEBUG Logging in file....")
logger.error("ERROR Logging in file....")
logger.critical("CRITICAL Logging in file....")

# message using f-string
f = "f-string"
logger.debug(f"This is {f} log message")
    
try:
    b = 1 / 0
except Exception as e:
    logger.error(f"Exception log as Error: {e}")


try:
    a = 1 / 0
except ZeroDivisionError as e:
    logger.exception(f"Exception log as exception with traceback: {e}")
