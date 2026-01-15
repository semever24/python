def isLoggedIn(func):
    def wrapper(*args):
        if LoggedIn:
            temp_func = func(*args)
            print(f'The output of the function is ==> {temp_func}')
        else:
            print(f'You need to Login')
    return wrapper


from time import time, sleep

def calc_execution_time(func):
    def wrapper(*args):
        initial_time = time()
        func(*args)
        exution_time = time() - initial_time
        print(f'It took {exution_time} for excution')
    return wrapper

LoggedIn = True

@isLoggedIn     # decorators function call
@calc_execution_time    # decorators function call
def add(num1, num2):
    sleep(3)
    print(num1 + num2)
    return add

@calc_execution_time
def sub(num1, num2):
    sleep(2)
    return num1 - num2

@calc_execution_time
def double(num1):
    sleep(5)
    return num1 ** 2

@calc_execution_time
def just_100():
    sleep(1)
    return 100

add(20, 500)