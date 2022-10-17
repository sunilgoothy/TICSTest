from TICSUtil import log_time, TICSLogger, emoji
import os, time


# print(log_time())

# New Method
# os.environ['LOG_FILENAME'] = "OSTEST.log"
log_dir = "D:\DevProjects\TICSTest\TICSUtil\logs"
# Logger = TICSLogger(filename="Test1.log", dir = log_dir)
Logger = TICSLogger(dir = log_dir)
# Log = TICSLogger(dir = log_dir).get_log
# Logger = TICSLogger()
Log = Logger.get_log
Log.info(f'Logger Configured...')
time.sleep(1)
Log.log(50 , f'Sample LOG message')
time.sleep(1)
Log.debug(f'Sample DEBUG message')
time.sleep(1)
Log.info(f'Sample INFO message')
time.sleep(1)
Log.warning(f'Sample WARNING message')
time.sleep(1)
Log.critical(f'Sample CRITICAL message')
time.sleep(1)
Log.info(emoji["namaste"])
time.sleep(1)

try:
    a = 1/0
except Exception as e:
    Log.exception(e)