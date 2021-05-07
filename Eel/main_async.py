# import gevent.monkey
# gevent.monkey.patch_all()

import eel

eel.init('web')

@eel.expose
def add(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum

@eel.expose
def chgText():
    for i in range(10):
        eel.sleep(1)
        eel.changeText(f"Hellooo from Python {i}")

if __name__ == "__main__":
    eel.start('index.html', size=(500,500))
    print("After eel start...")

