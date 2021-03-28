from time import sleep
import sys, os

#setting line buffering. 
# If we set buffering=0, it means the unbuffered. But it is only available in binary file mode (w->wb).
# We can use the line buffer to achieve a likely effect as the unbuffering policy.
# https://medium.com/@bramblexu/three-ways-to-close-buffer-for-stdout-stdin-stderr-in-python-8be694bd2737
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)

if __name__ == "__main__":
    for i in range(30):
        print(f'Counter ==> {i}')
        sleep(1)