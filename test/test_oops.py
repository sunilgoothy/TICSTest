
class Test:
    newvar = 10
    def __init__(self):
        self.newvar = 11

    var1 = 1
    var2 = 2

test1 = Test()
print(test1.var1)
print(test1.var2)
print(test1.newvar)
