import eel, threading, time, asyncio

eel.init('web')

@eel.expose
def add(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum

@eel.expose
def chgText():
    t1 = threading.Thread(target=chgTextThread, daemon = True)
    t1.start()

def chgTextThread():
    for i in range(10):
        time.sleep(1)
        eel.changeText(f"Hellooo from Python {i}")

if __name__ == "__main__":
    eel.start('index.html', size=(500,500))
    print("After eel start...")

