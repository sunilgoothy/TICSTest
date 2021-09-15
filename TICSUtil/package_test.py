from TICSUtil import log_time, TICSLogger, emoji
import os


print(log_time())

# New Method
# os.environ['LOG_FILENAME'] = "OSTEST.log"
log_dir = "D:\DevProjects\TICSTest\TICSUtil\logs"
# Logger = TICSLogger(filename="Test1.log", dir = log_dir)
# Logger = TICSLogger(dir = log_dir)
# Log = TICSLogger(dir = log_dir).get_log
Logger = TICSLogger()
Log = Logger.get_log
Log.info(f'Logger Configured...')
Log.log(50 , f'Sample LOG message')
Log.debug(f'Sample DEBUG message')
Log.info(f'Sample INFO message')
Log.warning(f'Sample WARNING message')
Log.critical(f'Sample CRITICAL message')
Log.info(emoji["namaste"])