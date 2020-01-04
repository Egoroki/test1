from random import randint
from time import sleep, time


def caching(timeout):
    def func_wrapper(fn):
        timing = 0
        word = ''
        cache = {timing: time(), word: fn()}

        def inner():

            if time() > cache[timing] + timeout:
                cache[word] = fn()
                cache[timing] = time()
            return cache[word]

        return inner

    return func_wrapper


@caching(timeout=3)
def func():
    return randint(0xFFFFFF, 0xFFFFFFF)

#
x = func()
assert x is func()
sleep(4)
assert x is not func()
