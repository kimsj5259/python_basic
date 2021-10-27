#WEEK 1
# 1.숫자를 입력하면 구구단을 실행하는 코드를 작성.
'''
print("구구단을 출력. \n")
for x in range(2, 10):
    print("----- [" +str(x) + "단] ------")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
print("-------------")

while True:
        num1 = input("num: ")
        for i in range(1, 10):
                print(num1, "X", i, "=", int(num1)*i)
'''                
# 2.금액을 입력하면 화폐나 동전 몇장(개)씩 필요한지 계산.
'''
li=[50000, 10000, 5000, 1000, 500, 100, 50, 10]
n=int(input('amount= '))
for i in li:
        m = n//i
        n = n%i
        if not m <= 0:          #불필요한 지,화폐는 표기 제거
                print(i,'---',m)
'''
# 3.3,6,9 게임을 실행하는 코드를 작성하시오.
'''
for n in range(1, 51):
        c=str(n).count('3')+str(n).count('6')+str(n).count('9')
        if c==0:
                print(n, end=' ')
        else:
                print('clab'*c, end=' ')
'''

# 4.네명의 나이와 점수 리스트.
'''
A={'age':30,'Korean':85,'English':90,'Math':90}
B={'age':29,'Korean':85,'English':95,'Math':100}
C={'age':30,'Korean':20,'English':99,'Math':80}
D={'age':30,'Korean':95,'English':90,'Math':92}


# C의 총점과 평균.

tot=A['Korean']+A['English']+A['Math']
avg=tot/3

print(tot)
print(avg)

# 모두의 나이의 합계.

tot=A['age']+B['age']+C['age']+D['age']
print(tot)

# 모든 점수 중 가장 낮은 점수는 몇점.

mini=100

for i in A,B,C,D:
    minimum=0
    if i['Korean']<i['English'] and i['Korean']<i['Math']:
        minimum=i['Korean']
    elif i['English']<i['Korean'] and i['English']<i['Math']:
        minimum=i['English']
    else:
        minimum=i['Math']
    print('min= ', minimum)

    if minimum<mini:
        mini=minimum
print('최소점수= ', mini)
'''



# 5.1~30 사이의 수에서 홀수만 더한 값, 짝수만 더한 값 구하기(while)
'''
x = 1
sum1 = 0
sum2 = 0
while x < 31:
    if x % 2 == 1:
        sum1 = sum1 + x
    elif x % 2 != 1:
        sum2 = sum2 + x
    x = x + 1
print(sum1)
print(sum2)

sum1 = 0
sum2 = 0
for i in range(1, 31):
    if i % 2 == 1:
        sum1 += i
    elif i % 2 != 1:
        sum2 += i
print(sum1)
print(sum2)
'''
# 6.예외처리 문법을 활용하여 정수가 아닌 숫자를 입력했을때 에러문구 나오게 작성
'''
while True:
    try:
        x = int(input("Enter a random number: "))
        break
    except ValueError:
        print("Oops, unverified number. Try again.")
'''
# 7.Input 함수를 활용하여 아이디와 비밀번호가 일치하면 '로그인 성공' 틀리면'로그인 실패' 문구가 나오는 코드.
'''
ID = 'Jin'
PW = 'pythonking'
a = input("Please enter your ID: ")
b = input("Please enter your PW: ")

if (a==ID) and (b==PW):
    print("Login successful")
else:
    print("Login failed")
'''

# 8.두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
'''
A = 20
B = 10

print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)
'''
# 9.두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
'''
A = int(input("1st random num: "))
B = int(input("2nd random num: "))

if A>B:
    print(str(A) +" is greater than "+ str(B))
elif A<B:
    print(str(A) +" is less than "+ str(B))
else:
    print("They are same.")
'''

# 10. 현재 날짜와 시간이 나온는 프로그램을 작성하시오.
'''
from datetime import datetime

print("year = {0}".format(datetime.today().year))
print("month = {0}".format(datetime.today().month))
print("day = {0}".format(datetime.today().day))
print("hour = {0}".format(datetime.today().hour))
print("min = {0}".format(datetime.today().minute))
'''
