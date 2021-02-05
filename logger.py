import logging
import sys

#Setup logger
Log = logging.getLogger('mylogger')
Log.addHandler(logging.FileHandler('mainlogger.log'))
Log.addHandler(logging.StreamHandler(sys.stdout))
Log.setLevel('DEBUG')


print("Starting Program.....")
Log.info("Info Logging....")
