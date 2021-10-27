"""
 for i in range(5):
   for j in range(5):
     print('j:', j,sep='', end=' ')  
   print('i:', i, '\\n', sep='')

 for i in range(3):
   for j  in range(7):
     print('#', end=' ')
   print()

 for i in range(1, 15):
   if i % 3 == 0:
     print('Fizz')
   elif i % 5 == 0:
     print('Buzz')
   else:
     print(i)

 for i in range(1, 51):
   print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

import turtle as t
 n = 6
 t.shape('turtle')
 t.color('light grey')
 t.begin_fill()
 for i in range(n):
   t.forward(100)
   t.right(360 / n)
 t.end_fill()
  
 import turtle as t
 n = 60
 t.shape('turtle')
 t.speed('fastest')
 for i in range(300):
   t.forward(i)
   t.right(91)

 'fastest': 0
 'fast': 10
 'normal': 6
 'slow': 3
 'slowest': 1

 word = input("please put the word: ")

 is_palindrome = True
 for i in range(len(word) // 2):
   if word[i] != word[-1 - i]:
     is_palindrome = False
     break

 print(is_palindrome)
"""

"""
 for i in range(len(text) - 3):
   print(text[i], text[i + 1], sep=' ')

 text = 'this is python script'
 words = text.split()

 for i in range(len(words) - 1):
   print(words[i], words[i + 1])

 a = int(input("Please enter your age: "))
 b = years_to_retirement = 65 - a
 c = year_of_retirement = 2020 + years_to_retirement

 print("You can retire " + str(years_to_retirement) + " years from now in " + str(year_of_retirement)  + ".")

 name = input("Please enter your name. ")
 first = name[0]
 last = name[-1]

 if first.upper() == last.upper():
   print("The name " + name +  " starts and ends with the same letter.")
 else:
   print("The name " + name +  " doesn't start and end with the same letter.")
"""

# 누적 연산자
#def calc():
#  a = 3
#  b = 5
#  total = 0
#  def mul_add(x):
#    nonlocal total
#    total = total + a * x + b
#    print(total)
#  return mul_add

#c = calc()
#c(1), c(2), c(3)

#class Person:
#  def __init__(self):
#    self.hello = "Hi"

#  def greeting(self):
#    print(self.hello)

#james = Person()
#james.greeting()

#함수 호출 과정
#def mul(a,b):
#    c = a * b
#    return c

#def add(a,b):
#    c = a + b
#    print(c)
#    d = mul(a,b)
#    print(d)

#x = 10
#y = 20
#add(x,y)

#위랑 같음
#def add(a,b):
#    c = a + b
#    print(c)

#def mul(a,b):
#    c = a * b
#    print(c)

#x = 10
#y = 20
#add(x,y)
#mul(x,y)

#재귀호출
#def hello(count):
#    if count == 0:
#        return
#    print('Ssup, world!', count)

#    count -= 1
#    hello(count)
#hello(5)

#재귀호출 팩토리얼(5!)
#def factorial(n):
#    if n == 1:
#        return 1
#    return n * factorial(n-1)
#print(factorial(6))

#람다 표현식
#plus_ten = lambda x : x + 10
#print(plus_ten(1))
# 서로 같음
#def plus_ten(x):
#    return x + 10
#print(plus_ten(1))

#람다map
#a = [1,2,3,4,5,6,7,8,9,10]
#list(map(lambda x: str(x) if x % 3 == 0 else x, a))

#람다filter
#a = [8,3,2,10,15,7,1,9,0,11]
#list(filter(lambda x: x > 5 and x < 10, a))

#reduce
#def f(x,y):
#    return x + y
#a = [1,2,3,4,5]
#from functools import reduce
#reduce(f,a)

#reduce의 람다 표현
#a = [1,2,3,4,5]
#from functools import reduce
#reduce(lambda x, y: x + y,a)

#클로저 (global 전역변수)
#x = 10
#def foo():
#    global x
#    x = 20
#    print(x)  
#foo()
#print(x)

#함수 안에서 함수
#def print_hello():
#    hello = 'Hello, world'  # <<지역변수
#    def print_message():
#        print(hello)
#    print_message() # hello에 접근할 수 있는 범위
#print_hello()

#def A():
#    x = 10      # A의 지역 변수 x
#    def B():
#        nonlocal x  # 현재 함수의 바깥쪽에 있는 지역 변수 사용
#        x = 20      # A의 지역 변수 x에 20 할당
#    B()
#    print(x)
#A()

#def A():
#    x = 10
#    y = 100
#    def B():
#        x = 20
#        def C():
#            nonlocal x  # x 와 y 의 가장 가까운 값
#            nonlocal y
#            x = x + 30
#            y = y + 300
#            print(x)
#            print(y)
#        C()
#    B()
#A()

#def calc():
#    a = 3
#    b = 5
#    def mul_add(x):
#        return a * x + b
#    return mul_add

#def calc():
#    a = 3
#    b = 5
#    return lambda x: a * x + b
#c = calc()
#print(c(1), c(2), c(3), c(4), c(5))

#누적 = (합의 누적)
#def calc():
#    a = 3
#    b = 5
#    total = 0
#    def mul_add(x):
#        nonlocal total
#        total = total + a * x + b
#        print(total)
#    return mul_add
#c = calc()
#c(1)
#c(2)
#c(3)

#Class & Method ** (int,list,dict 등도 Class)
#class Person:
#    def __init__(self, name , age, address, wallet):
#        self.name = name
#        self.age = age
#        self.address = address
#        self.__wallet = wallet # 변수 앞에 __을 붙여서 비공개 속성으로 만듦

#    def pay(self, amount):
#        self.__wallet -= amount #비공개 속성은 클래스 안의 메서드에서만 접근
#        print('이제 {0}원 남았네요.'.format(self.__wallet))

#    def pay(self, amount):
#        if amount > self.__wallet:
#            print('money lack...')
#            return
#        self.__wallet -= amount
        
#maria = Person('마리아', 20, '35 blvd, Seoul', 10000)
#maria.pay(3000)

#Class 속성과 인스턴스 속성
#class Person:
#    bag = []

#    def put_bag(self, stuff):
#        self.bag.append(stuff)

#james = Person()
#james.put_bag('책')
#maria = Person()
#james.put_bag(' 열쇠')

#print(james.bag)
#print(maria.bag)

#class Knight:
#    __item_limit = 10

#    def print_item_limit(self):
#        print(Knight.__item_limit)

#x = Knight()
#x.print_item_limit()
#print(Knight.__item_limit)

#정적메서드
#class Calc:
#    @staticmethod
#    def add(a, b):
#        print(a + b)

#    @staticmethod
#    def mul(a, b):
#        print(a * b)
#Calc.add(10, 20)
#Calc.mul(10, 20)
              
#클래스메서드
#class Person:
#    count = 0

#    def __init__(self):
#        Person.count += 1

#    @classmethod
#    def print_count(cls):
#        print('{0}명 생성되었습니다.'.format(cls.count))

#james = Person()
#maria = Person()
#Person.print_count()

#사람목록관리 클래스
#class Person:
#    def greeting(self):
#        print("Heyy.")
        
#class PersonList():
#    def __init__(self):
#        self.person_list = []

#    def append_person(self, person):
#        self.person_list.append(person)

#메서드 오버라이딩
#class Person:
#    def greeting(self):
#        print('안녕하세요')
#class Student(Person):
#    def greeting(self):
#        super().greeting()
#        print('저는 파이썬 코딩 도장 학생입니다.')

#james = Student()
#james.greeting()

#다중 상
#class Person:
#    def greeting(self):
#        print('Hey')

#class University:
#    def manage_credit(self):
#        print('credit managing.')

#class Undergraduate(Person, University):
#    def study(self):
#        print('Study')

#james = Undergraduate()
#james.greeting()        #Hey.:기반 클래스 Person의 메서드 호출
#james.manage_credit()   #credit managin: 기반 클래스 University의 메서드 호출
#james.study()           #Study: 파생 클래스 Undergraduate에 추가한 study 메서

#class A:
#    def greeting(self):
#        print('Hey, its A.')

#class B(A):
#    def greeting(self):
#        print('Hey, its B.')

#class C(A):
#    def greeting(self):
#        print('Hey, its C.')

#class D(C, B):
#    pass

#x = D()
#x.greeting()
# mro(Method Resolution Order) 사용해서 탐색 순서 알아보기

#추상 클래스 사용
#from abc import*

#class StudentBase(metaclass=ABCMeta):
#    @abstractmethod
#    def study(self):
#        pass
 
#    @abstractmethod
#    def go_to_school(self):
#        pass

#class Student(StudentBase):
#    def study(self):
#        print('STUDY')

#    def go_to_school(self):
#        print('Go to school')

#james = Student()
#james.study()
#james.go_to_school()

#두 점 사이의 거리
#import math

#class Point2D:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

#p1 = Point2D(x=30, y=20)    #점1
#p2 = Point2D(x=60, y=50)    #점2

#a = p2.x - p1.x         #선 a의 길이
#b = p2.y - p2.x         #선 b의 길이

#c = math.sqrt((a * a) + (b * b))    #(a*a) + (b*b)의 제곱근을 구함
#print(c)        #42.42654...

#c = math.sqrt(math.pow(a, 2) + math.pow(b, 2)) << =math(a**2) + (b**2)

##*예외처리 사용하기
#try:
#    x = int(input('나눌 숫자를 입력하세요:'))
#    y = 10 / x
#    print(y)
#except:
#    print('예외가 발생했습니다.')

#y = [10, 20, 30]

#try:
#    index, x = map(int, input('인덱스와 나눌 숫자를 입력: ').split())
#    print(y[index] / x)
#except ZeroDivisionError as e:
#    print('숫자를 0으로 나눌 수 없다.', e)
#except IndexError as e:
#    print('잘못된 인덱스입니다.', e)
                   
##파이썬 예외 계층도:
 #   BaseExeception:
 #       SystemExit
 #       KeyboardInterrupt
 #       GeneralExit
 #       Exception:
 #           StopIteration
 #           ArithmeticError:
 #               ZeroDivisionError
 #           LookupError:
 #               IndexError
 #           SyntaxError

## else & finally 사용
#try:
#    x = int(input('number to divide: '))
#    y = 10 / x
#except ZeroDivisionError:
#    print('cant divided by 0.')
#else:
#    print(y)
#finally:
#    print('코드 실행이 끝났습니다.')

#예외 발생시키기
#def three_multiple():
#    try:
#        x = int(input('3의 배수를 입력: '))
#        if x % 3 != 0:
#            raise Exception('3의 배수가 아닙니다.')
#        print(x)
#    except Exception as e:
#        print('three_multiple 함수에서 예외가 발생했습니다.', e)
#        raise

#try:
#    three_multiple()
#except Exception as e:
#    print('스크립트 파일에서 예외가 발생했습니다,', e)

##예외 만들기
#class NotThreeMultipleError(Exception):
#    def __init__(self):
#        super().__init__('3의 배수가 아닙니다.')

#def threeMultiple():
#    try:
#        x = int(input('3의 배수를 입력: '))
#        if x % 3 != 0:
#            raise NotThreeMultipleError
#        print(x)
#    except Exception as e:
#        print('예외가 발생했습니다.', e)

#three_multiple()

#이터레이터(iterator) = 값을 차례대로 꺼낼 수 있는 객체 dir(객체) StopIterarion(끝)
#이터레이터는 클래스에 __iter__, __next__, __getitem__
#class Counter:
#    def __init__(self, stop):
#        self.current = 0
#        self.stop = stop

#    def __iter__(self):
#        return self

#    def __next__(self):
#        if self.current < self.stop:
#            r = self.current
#            self.current += 1
#            return r
#        else:
#            raise StopIteration

#for i in Counter(3):
#    print(i, end= ' ')

#class Counter:
#    def __init__(self, stop):
#        self.stop = stop
#    def __getitem__(self, index):
#        if index < self.stop:
#            return index
#        else:
#            raise IndexError
#print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

#for i in Counter(3):
#      print(i, end=' ')

# iter, next 함수 활용하기 
#import random

#while True:
#    i = random.randint(0, 5)
#    if i == 2:
#        break
#    print(i, end=' ')

## 제너레이터 = 이터레이터를 생성해주는 함 (yield만 사용)

#def number_generator(stop):
#    n = 0
#    while n < stop:
#        yield n
#        n += 1

#for i in number_generator(3):
#    print(i, end= ' ')
# above is same as using "next"

#def number_generator(stop):
#    n = 0
#    while n < stop:
#        yield n
#        n += 1

#def three_generator():
#    yield from number_generator(3)

#for i in three_generator():
#    print(i)

# 코루틴은 제너레이터의 특별한 형
#def number_coroutine():
#    while True:
#        x = (yield)
#        print(x, end=' ')

#co = number_coroutine()
#next(co)

#for i in range(20):
#    co.send(1)

#co.close()


#def sum_coroutine():
#    try:
#        total = 0
#        while True:
#            x = (yield)
#            total += x
#    except RuntimeError as e:
#        print(e)
#        yield total     # 코루틴 바깥으로 값 전달

#co = sum_coroutine()
#next(co)
#for i in range(20):
#    co.send(i)
#print(co.throw(RuntimeError, 'off with exception')) 

#데코레이터 (매개변수와 반환값을 처리)
#class Trace:
#    def __init__(self, func):
#        self.func = func

#    def __call__(self,*args, **kwargs):
#        r = self.func(*args, **kwargs)
#        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))                 
#        return r

"""
@Trace
def add(a, b):
    return a + b
print(add(10, 20))
print(add(a=10, b=20))

class IsMultiple:
    def __init__(self, x):      # 데코레이터가 사용할 매개변수를 초깃값으로
        self.x = x              # 매개변수를 속성 x에 저장

    def __call__(self, func):   # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):      # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a, b)      # func를 호출하고 반환값을 변수에 저장
            if r % self.x == 0: # func의 반환값이 self.x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수.'.format(func.__name__, self.x))
            else:
                print("{0}의 반환값은 {1}의 배수가 아니다.".format(func.__name__, self, x))
            return r            # func의 반환값을 반환
        return wrapper          # wrapper 함수 반환

@IsMultiple(3)      # 데코레이터(인수)
def add(a, b):
    return a + b

print(add(10, 20))
print(add(2, 5))
"""

# re 모듈을 가져와서 판단
# re에서 문자는 ^ 로 범위 설정, 숫자는 *$ 로

### *import로 모듈 가져오기*

# python = NumPy
# python database = Sybase, Infomix, Oracle, MySQL, PostgreSQL

#while 문
'''
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("Hit the tree %d-time." % treeHit)
    if treeHit == 10:
        print("Tree has been fallen.")
'''

def GuGu(n):
    result = []
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result

print(GuGu(2), end=' ')

a = "a:b:c:d"
b = a.split(":")
print(b)

c = "#".join(b)
print(c)

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

cal1 = Calculator([1,2,3,4,5])
cal1.sum()

call.avg()

cal2 = Calculator([6,7,8,9,10])
cal2.sum()

cal2.avg()

result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivsionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4
print(result)

'''
def ex_while():
    i=2
    j=1
    while i<10:
        while j<10:
            print('{} X {} = {}'.format(i, j, i*j))
            j += 1
        j = 1
        i += 1
def ex_for():
    for i in range(2,10):
        for j in range(1,10):
            print('{} X {} = {}'.format(i, j, i*j))
def ex_break():
    n = 2
    loof = True
    while loof :
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        n +=1 # 이거 위치가 continue랑 다름
        con=input(str(n)+'단을 출력하시겠습니까?(Y/N) : ')
        if con == 'N':
            break
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        loof = False
    print('구구단이 종료 되었습니다.')
def ex_continue():
    n = 2
    loof = True
    while loof :
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        con=input(str(n)+'단을 다시 출력하시겠습니까?(Y/N) : ')
        if con == 'Y':
            continue
        n += 1
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        loof = False
    print('구구단이 종료 되었습니다.')
ex_break()
'''


 
            

