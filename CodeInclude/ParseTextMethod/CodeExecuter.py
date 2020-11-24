from TICSUtil import *
import sys
import io


if __name__ == '__main__':
    # initialization
    # this variable will be exposed as api to external code
    global_var = 123

    # Execution Module
    # create file-like string to capture output
    # codeOut = io.StringIO()
    # codeErr = io.StringIO()
    with open('code.txt', 'r') as file:
        lines = file.readlines()
    code = ''
    for line in lines:
        code = code + line

    try:
        exec(code)
    except Exception as e:
        print(f'Exception in executing the code, msg={e}')

    try:
        print(func(2))
    except Exception as e:
        print(f'Exception in calling function, msg={e}')

    print("-" * 80)
    test = Test()
    test.increase()
    print("test var:", test.var)

    try:
        test.raise_error()
    except Exception as e:
        print(e)

    print(division(10, 2.5))

    print(multiply(10))

    funcPrint('This function is executed from a code within txt file')


    print(global_var)
