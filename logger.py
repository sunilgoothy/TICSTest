import logging
import sys


#Setup logger
mainlogger = logging.getLogger('mylogger')
mainlogger.addHandler(logging.FileHandler('mainlogger.log'))
mainlogger.addHandler(logging.StreamHandler(sys.stdout))
mainlogger.setLevel('DEBUG')


print("Starting Program.....")
mainlogger.info("Info Logging....")
