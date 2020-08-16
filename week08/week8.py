作业一：
# 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

# list
# tuple
# str
# dict
# collections.deque


#容器序列：list,tuple,ollections.deque


#扁平序列：str

#可变序列：list,collections.deque
#不可变序列：tuple,str



作业二：
def Map1(f,List):
    for i in range(len(List)):
        yield f(List[i])

def f(x):
    return x**3

List = [1,2,3,4,5]

for i in map(f,List):
    print(i)


for i in Map1(f,List):
    print(i)



作业三：
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def time_this_func(*args, **kwargs):
        print('timer of decorator...')

        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'@timer: {func.__name__} took {end_time - start_time: .5f} s')
        return res

    return time_this_func


@timer
def time_test_func(n):
    while n > 0:
        time.sleep(0.1)
        n -= 1


time_test_func(100)