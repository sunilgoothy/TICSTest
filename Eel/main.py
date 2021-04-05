import eel

eel.init('web')

@eel.expose
def add(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum

if __name__ == "__main__":
    eel.start('index.html', size=(500,500))    

