# Week 2 (Simple Algorithm)

#1. 입력을 정수 n 으로 받았을 때, n 이하 까지의 피보나치 수열을 출력하는 함수를 작성하세요.
'''
def number(n):

    if n==0:
        return 0
    if n==1:
        return 1
    return number(n-1)+number(n-2)

num=int(input("Any integer: "))

for i in range(num):
    print(number(i), end=' ')
'''
#2. 사용자로부터 주민등록번호를 입력 받아 출생 연도를 출력하세요.
'''
ID = '010525-3234567'
yy=int(ID[0:2])
if ID[7] in ('1', '2'):
    print('출생 연도는:19',yy,'년')
elif ID[7] in ('3', '4'):
    print('출생 연도는:20',yy,'년')
'''
#3. 연도가 주어졌을 때 윤 년이면 1, 아니면 0을 출력하는 프로그램을 작성하세요.
#    - (윤년 = 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때)
'''
yy = int(input())
if yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0:
    print('1')
else:
    print('0')
'''

#4. 1부터 100 사이의 숫자를 하나 랜덤하게 생성하고, 이를 맞추는 게임을 작성하세요.
#    - 숫자를 하나 생성하고, 그 다음 사용자가 숫자를 입력하면 이 둘을 비교하여 ‘높음’, ‘낮음’, ‘맞췄다’를 출력해야 한다.
#    - 또한, 몇 번의 guess 끝에 답을 맞췄는 지 시도한 횟수를 값으로 출력해야 한다.
'''
import random
randompick = random.randrange(1, 101)
print("selected num is {} .".format(randompick))
random_num = int(input("random number : "))
print("which is {}.".format(random_num))

trial = 0
while True:
    trial += 1
    if random_num < randompick:
        print("높음")
        random_num = int(input("type another: "))
    elif random_num > randompick:
        print("낮음")
        random_num = int(input("type another: "))
    else:
        print("맞췄다")
        break
print("Got it after {} attempts.".format(trial))
'''
#5. 사용자로부터 달러 또는 위안 금액을 입력 받은 후 이를 원으로 바꿔서 계산하세요.
#    - 사용자는 100 달러, 100 위안 과 같이 금액과 통화 명 사이에 공백을 넣어 입력 하기로 합니다.
#    - 각 통화 별 환율:  달러- 1112원, 위안 - 171원
'''
a = input("please add 'USD' or 'CNY' behind the amount: ")
i = a.split()
if 'USD' in i:
    b = float(i[0]) * 1112
    print('which is ', b ,' KRW')
elif 'CNY' in i:
    c = float(i[0]) * 171
    print('which is ', c ,' KRW')
'''

#6. 로또번호 6개를 무작위로 생성하세요(1~45)(중복X)
'''
import random
num = list(range(1, 7))
number = []
for i in range(6):
    number.append(num.pop(num.index(random.choice(num))))
print('로또번호: ', number)

import random
number=[]
while len(number)<6:
    num=random.randint(1, 46)
    if num not in number:
        number.append(num)
print('로또번호: ', number)

import random
number = set()
while len(number)<6:
    number.add(random.randint(1,46))
print('로또번호: ',number)

import random
import itertools
numbers = list(itertools.combinations(range(1,46),6))
print('로또번호: ',number)
'''
#7. 점수를 입력했을 때 점수가 85점 이상이면 합격, 이하면 불합격이 나오게 작성하세요.
'''
a = int(input("score: "))
if a >= 85:
    print("pass.")
else:
    print("fail.")
'''
#8. 별찍기.  *로 입력한 숫자만큼 높이가 n인 삼각형을 출력하세요.
'''
for n in range(1,10):
    print('*' * n)

for n in range(1,10):
    print(' '*(9-n) + '*'*n)

for n in range(1,10):
    print(' '*(9-n) + '*'*(2*n-1))    
'''
#9. 전화번호를 입력받을때 뒤에4자리를 제외하고는 *로 가려지게 작성하세요.(9~11자리)
'''
number = input('number: ')
fix_nums = '*' * (len(number)-4)
print(fix_nums + number[-4:])
'''
#10. 리스트 a=[1,1,1,1,2,2,3,3,3,4,4,5,5,5] 에서 중복숫자를 제거한 [1,2,3,4,5] 리스트를 만드세요.
'''
a=[1,1,1,1,2,2,3,3,3,4,4,5,5,5]
print(list(set(a)))
'''
'''
number = input('전화번호')
fixed_number = '*' * (len(number)-4)
print (fixed_number + number[-4:])
'''
'''
=========== 
PN = "010-7764-9954"
i = 0
n= int(len(PN))
while i < n-4:
    if PN[i] != '-':
        PN_re = PN.replace(PN[i],'*',1)
        i = i +1
        PN = PN_re
    else:
        i = i + 1
print(PN_re)
'''

v_machine = {'water':300,'coffee':500,'s.water':400,'coke':450,'fanta':350}
i = 1
input_amount = int(input('insert coins: '))
products = input('choose products: ')
change = input_amount - v_machine[products]

#돈 모자라면 못 뽑음  
while i < 4:
    if input_amount > v_machine[products]:
        print ('get your',products,'change: ',change) 
        input_amount = change
        products = input('choose products: ')
        change = input_amount - v_machine[products]
    elif input_amount < v_machine[products]:
        print('need more coins')
        break
    else:
        print ('get your',products,'change: ',change)
        break
    i += 1 
    if i >= 4:
      print('exit')

#모자란 돈을 더 넣어서 뽑는 경우 : 세 가지 선택 불가.. 
while i < 4:
    if input_amount > v_machine[products]:
        print ('get your',products,'change: ',change) 
        input_amount = change
        products = input('choose products: ')
        change = input_amount - v_machine[products]
    elif input_amount < v_machine[products]:
        need = v_machine[products] - input_amount
        print('need more coins: ',need)
        input_amount_second = int(input('insert more coins: '))
        input_amount = input_amount_second + input_amount
        change = input_amount - v_machine[products]   
    elif change == 0:
        print ('get your',products,'change: ',change)
        break

    i += 1 
    if i >= 4:
      print('exit')
