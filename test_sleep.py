import datetime as dt 
import time

st = time.perf_counter()
for i in range(10):
    time.sleep(0.001)
    # pass
    
end = time.perf_counter()
elapsed = (end-st) * 1000
print("Total time taken(msec):", elapsed)