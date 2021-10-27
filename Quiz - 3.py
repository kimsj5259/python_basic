#1.A=[1, 11, 13, 14, 15, 16, 111, 0.7) 최대값과 최소값을 구하세요.
'''
A=[1, 11, 13, 14, 15, 16, 111, 0.7]
print(max(A), min(A))
'''
#2.13자리의 주민 등록번호를 입력 후 성별(남자, 여자)를 출력하는 프로그램을 작성하세요.
'''
a = input("ID num: ")
if a[7] == '1'and '3':
     print("guy")
if a[7] == '2'and '4':
     print("lady")
'''
'''
resident_number = input("주민등록번호를 입력해주세요 ")
resident_number = resident_number.split("-")[1]
if resident_number[0] == "1" or resident_number[0] == "3":
    print("남자")
else:
    print("여자")
'''
#3.임의의 체중과 신장을 입력한후 비만도를 출력하는 함수를 작성하세요
'''                    
height=float(input("height: "))
weight=float(input("weight: "))

BMI = weight/(height**2)

if BMI <18.5:
    print("skinny")
elif 18.5 <= BMI < 25.0:
    print("standard")
elif 25.0 <=BMI < 30.0:
    print("obesity")
elif BMI >= 30.0:
    print("Altitude obesity")
'''
#4.파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하세요. 
'''
list = ['intra.h', 'intra.c', 'define.h', '[run.py](http://run.py/)']
for values in list:
    split = values.split(".")
    if split[1] == "h" or split[1] == "c":
        print(values)
'''
#5.중첩 반복문을 사용하여 신문을 배달하는 프로그램을 작성하세요. 단 미납금이 있는 호수에는 배달 x
#apart=[[101,102,103,104],[201,202,203,204],[301,302,303,304],[401,402,403,404]]
#Unpaid=[101,202,302,403]
#출력 예) 101호:미납 102호:배달 103호: 배달
'''
apart=[[101,102,103,104],[201,202,203,204],[301,302,303,304],[401,402,403,404]]
Unpaid=[101,202,302,403]

for paid in apart:
    for unpaid in paid:
        if unpaid in Unpaid:
            print(unpaid, ': 미납')
        else:
            print(unpaid, ': 배달')
'''    
#6.자연수 n을 입력 했을 때 124 나라에서 사용하는 숫자로 바꾸세요.
## YET
'''
def solution(x):                                                                                         
    assert x > 0 

    maxDigit = 1 
    remain = x - 1 
    digitCheck = 3 
    while True:
        if int(remain / digitCheck) == 0:
            break

        remain -= digitCheck
        digitCheck *= 3
        maxDigit += 1

    resultList = list()
    digit = maxDigit
    while digit >= 1:
        digitCheck /= 3
        digitNum = int(remain / digitCheck)
        if digitNum == 0:
            resultList.append('1')
        elif digitNum == 1:
            resultList.append('2')
        else: # digitNum == 2:
            resultList.append('4')
                
        remain -= digitNum * digitCheck
        digit -= 1

    return ''.join(resultList)
'''
#7.국가 전체 예산 M을 정하고, 4개 지방에서 요청하는 예산을 각 각 정한 후 국가
#전체를 최대로 사용 할 수 있는 지방예산의 상한액을 정하는 프로그램을 작성하시오.
'''
national_budget = 485
local_budget1 = 120
local_budget2 = 110
local_budget3 = 140
local_budget4 = 150
#ceiling = 127
mean = int(national_budget) / 4

if national_budget >= mean:
    a = national_budget - mean
    if a >= mean:
        b = a - mean
        if b >= mean:
            c = b -mean
            if local_budget1 <= c:
                print("local_budget1 120 is allocated")
            if local_budget2 <= c:
                print("local_budget2 110 is allocated")
            if local_budget3 <= c:
                print("local_budget3 140 is allocated")
            else:
                
                print("local_budget3 " + str((national_budget - (local_budget1 + local_budget2))/2) + " is allocated instead")
            if local_budget4 <= c:
                print("local_budget4 150 is allocated")
            else:
                print("local_budget4 " + str((national_budget - (local_budget1 + local_budget2))/2) + " is allocated instead")
print("ceiling is "+str((national_budget - (local_budget1 + local_budget2))/2))
'''
#8.n 개의 100 이하의 자연수를 입력하고, 그 수들의 최소 공배수를 구하시오.
'''
from math import gcd

x=[int(x) for x in input("Enter multiple values: ").split()]
lcm=x[0]
def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)
    
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]
print(solution(x))
'''
#9.자연수 n을 입력하고, 자연수 n의 약수들의 총 합을 구하시오.
'''
input_int = int(input())
print(input_int, "의 약수", sep="")

total = 0
for x in range(1, input_int + 1):
    if input_int % x == 0:
        print(x)
        total += x
print(total)
'''
'''
def sumDivisor(num):
    answer = 0
    for i in range(1,num+1):
        if num%i==0:
            answer += i
    return answer
'''

#10.자판기 알고리즘
'''
drink = 3
coin=int(input('please insert the coin: '))
americano = 100
latte = 150

while True:
    if drink>=1:
        choice=int(input('please choose the drink\n1.americano\n2.latte\n'))
        print(str(choice)+' is chosen')
        if choice == 1 and coin>=americano :
            print('Ur americano is ready')
            drink-=1
            coin-=americano
        elif choice == 2 and coin>=latte:
            print('Ur latte is ready')
            drink-=1
            coin-=latte
        elif coin<latte or coin<americano:
            print('lack of money')
        else:
            print('not in the menu')
            continue
        print(str(coin)+' is your change')
        choice = str(input('please press the E button to receive your change or press another button to proceed further'))
        if choice == 'E':
            print(str(coin)+' is your change')
            break
    else:
        print('lack of coffee')
        break
'''
#* 다른 사람 코드 *
'''
menu = {'콜라': 1000, '사이다':500,'환타':1500, '핫식스':2000}
ks = menu.keys()
key_list = list(menu.keys())
vals = menu.values()

for k in ks:
    print('메뉴명:%s, 가격:%d' %(k,menu[k]))
money = int(input('돈을 투입하세요'))
n = input('메뉴를 입력하세
          요:')
if n in menu:
    print('%s의 가격은 %d입니다.' %(n,menu[n]))
    j = int(money) - int(menu[n])
    print('남은 잔돈은', j, '입니다')
    while True:
        for i in vals:
            if j >= i:
                n2 = input('음료를 추가로 구매하세요')
                j -= int(menu[n2])
                print('남은 잔돈은', j, '입니다')
            elif j == 0:
                print('잔액이 0원 입니다.')
                break
            else:
                print('잔액이 부족합니다.')
                break
        break
'''
'''
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0

print(solution(input("alphabet: ")))
'''

def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0
print(solution(input(": ")))