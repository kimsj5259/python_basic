# genertor
'''
def topten():
    yield 1
    yield 2
    yield 3
    yield 4

values = topten()

print(values.__next__())
print(values.__next__())


def topten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1

values = topten()

for i in values:
    print(i)
'''
import time

def print_iter(iter):
    for element in iter:
        print(element)

def lazy_return(num):
    print("sleep 1s")
    time.sleep(1)
    return num

print("comprehension_list=")
comprehension_list = [ lazy_return(i) for i in L ]
print_iter(comprehension_list)

print("generator_exp=")
generator_exp = ( lazy_return(i) for i in L )
print_iter(generator_exp)