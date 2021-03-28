import threading
import time, os

COUNT = 0
RUN = True
def input_read():
    global RUN
    while RUN:
        cmd = input("Enter your Command:")
        os.system('cls')
        if (cmd.upper() == 'STOP'):
            RUN = False
            print(f"STOP command issued...")
        elif (cmd.upper() == 'COUNT'):
            print(f"Now the count is {COUNT}")
        else:
            print(f"Enter Valid Command!!!")
        # time.sleep(0.1)
    print(f"input thread exited")

if __name__ == "__main__":
    print(f"RUN status {RUN}")
    in_thread = threading.Thread(target=input_read)
    in_thread.start()
    while RUN:
        COUNT+=1
        time.sleep(0.1)
    print(f"main thread exited")

    