# iterator - 이터레이터는 값을 순차적으로 꺼내올 수 있는 객체 입니다. 
'''
#L이라는 다음 리스트가 있을때 for loop문으로 값마다 제곱을 하는 코드는 다음과 
L = [1, 2, 3]
for x in L:
    print(x ** 2, end=' ')


#L 리스트가 반복 가능한 객체인지 확인해보는 방법은 dir 로 호출하여 __iter__ 함수가 있는지 확인해볼 수 있습니다.

L=['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
 '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
 '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


#dir로 출력해보면 __iter__ 함수가 들어있는 것을 확인할 수 있습니다. 그리고 직접 __iter__ 함수를 출력한 것을 print문을 사용해서 출력해보면 이터레이터 객체임을 확인할 수 있습니다.


print(L.__iter__())
#<list_iterator object at 0x10a999210>


#이터레이터를 변수에 저장후에 __next__ 함수를 호출하면 for문이 동작하는 것처럼 값을 하나씩 꺼내올 수 있습니다. 우선 dir 로 변수에 저장한 이터레이터를 확인해보겠습니다. print문으로 확인해보면 __next__ 함수가 들어있는 것을 확인할 수 있습니다. 그럼 __next__ 함수는 어떤일을 할 수 있을까요 ? 맞습니다. 다음 요소를 하나씩 꺼내오는 함수 입니다.

iterator_L = L.__iter__()
print("dir iterator_L = ", end=""), print(dir(iterator_L))


print(iterator_L.__next__())
print(iterator_L.__next__())
print(iterator_L.__next__())
print(iterator_L.__next__())
'''
# L 리스트에 iter와 next를 적용해서 for loop 으로 제곱한 것을 while문으로 구현
'''
L=['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
 '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
 '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

I = iter(L)
while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print( X**2, end=" ")
'''

#another example for iterator
'''
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

values = TopTen()
print(next(values))
'''

D = {'a':1, 'b':2, 'c':3}
#for key in D.keys():
#    print(key)

it = iter(D)
while True:
  try:
    x=next(it)
  except StopIteration:
    break
  print(x)
