import sys
from TICSutil import log_time
import logging

print(sys.path)

event_dict = dict()

class TICSEvents:
    def event_1(self):
        print(log_time(), "event_1 executed")
        return 1000

    def event_2(self):
        print(log_time(), "event_2 executed")

    def event_3(self):
        print(log_time(), "event_3 executed")

    def event_4(self):
        print(log_time(), "event_4 executed")

    def event_5(self):
        print(log_time(), "event_5 executed")

    def event_6(self):
        print(log_time(), "event_6 executed")

    def event_7(self):
        print(log_time(), "event_7 executed")

    def event_8(self):
        print(log_time(), "event_8 executed")

    def event_9(self):
        print(log_time(), "event_9 executed")

    def event_10(self):
        print(log_time(), "event_10 executed")


if __name__ == '__main__':
    evt_class = TICSEvents()

    for i in range(1, 10):
        event_dict[i] = f"event_{i}"

    print(event_dict)

    for key in event_dict:  
        f = getattr(evt_class, event_dict[key])         # get function name from dict using key and get its attribute as method into f.
        print(f())                                      # Execute the method by placing () at the end. If something is returned then it is printed.
        
