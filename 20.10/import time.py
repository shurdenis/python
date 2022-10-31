import time 


def times(a):
    def time2():
        start = time.time()
        a()
        end = time.time()-start
        print(end)
    return time2


@times
def func_to_decor():
    for i in range(1000):
        print(i)


func_to_decor()