#1.사이트별 비밀번호 프로그램
'''
web=input('any website: ')

a = web.lstrip('http://')
b = a.rstrip('.com')
c = b[0:3] + str(len(b)) + str(b.count('e')) + '!'
    
print(c)
'''
#2.kako 서비스를 이용하는 택시기사. 50명의 승객과 매칭 기회가 있을때, 아래 조건 만족하는 승객수
# a.승객별 운행 소요 시간은 5~50분 사이의 난수
# b.당신은 소요시간 5~15분 사이의 승객만 매칭
'''
from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님(소요시간: {1}분)".format(i, time))
        cnt += 1
    else:
        print("[] {0}번째 손님(소요시간: {1}분)".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))

#3.Class 안에 두개의 객체가 싸우는 프로그램

#마린: 공격 유닛, 군인. 총을 쓸 수 있음
'''
'''
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self. hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
'''
'''
class Unit:
    def __init__(self, name, job, hp):
        self.name = name
        self. job = job
        self. hp = hp
        print("이름:{0}, 직업: {1}, hp: {2}".format(self.name, self.job, self.hp))

    def attack(self, enemy):
        self.hp = 10
        print("{0} 이 {1}에게 10 피해를 입혔다.".format(self.name, enemy))

    def defense(self, name):
        damaged = 5
        print("{0}은 5 피해를 입었다.".format(self.name))

attacker = Unit('Jin', 'Berserker', 100)
defender = Unit('Joon', 'idiot', 100)
attacker.attack('Joon')
defender.defense('Joon')
'''

#4.Seoul의 element 중 Kim의 위치 x를 찾아, 김서방은 x에 있다를 반환 하는 함수.
# ex) Seoul = ['Jane', 'Kim']   return "김서방은 1에 있다"
                  
# 피보나치 수열 
'''
a = []
def fib(n):
    for i in range(n+1):
        if i == 0:
            a.append(0)
        elif n==1 or n==2:
            a.append(1)
        else:
            a.append(a[n-1] + a[n-2])

    return a[n]
print(
'''
'''
counter = 0
def fib(n):
    global counter
    counter += 1
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return n

print(fib(3))
print(counter)
'''
'''
>> fib(5)
>> fib(4) + fib(3)
>> (fib(3) + fib(2)) + fib(3)
>> ((fib(2) + fib(1)) + fib(2) + fib(3)
>> (((fib(1) + fib(0)) + fib(1)) + fib(2)) + fib(3)
1단계: ((1 + 0) + 1) + fib(2) + fib(3)
2단계: (2 + (fib(1) + fib(0))) + fib(3)
3단계: (2 + (1 + 0)) + fib(3)
4단계: 3 + 2(*위에fib(3)을 찾으세요)
5단계: 5
'''
#재귀함수의 전형적인 문제: n의 숫자만큼 2의 n승 만큼 호출하기 때문에 시간이 상당히 걸
#counter라는 변수를 만들어 계산이 몇번 이루어지는지 알아보기


#재귀함수의 문제점을 해결해주는 **메모화(memoization)
'''
메모 = { 1: 1, 2:1 }
def fib(n):
    if n in 메모:
        return 메모[n]
    else:
        output = fib(n-1) + fib(n-2) #아웃풋이라는 변수에 저장
        메모[n] = output          # 한번 저장 했던 값이니까
        return output
print(fib(100))
'''
#이는 한번 계산 했던 것은 다시 계산하지 않고, 메모 했던 것을 확인하기 때문이


# 계좌 문제(def 활용)
'''
def open_account():
    print("new account has been created.")

def deposit(balance, money): #입금
    print("deposit is completed. now you have {0} dollars.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("withdraw is completed. now you have {0} dollars.".format(balance =money))
    else:
        print("withdraw is not completed. now you have {0} dollars.".format(balance))
        return balance

def withdraw_night(balnce, money): #저녁에 출금
    commission = 100
    return commision, balance - money - commission

balance = 0 #잔액
balance = deposit(balance, 1000)
#balance = widthdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("charge {0}, and now you have {1} dollars.".format(commision, balance))
'''


#지선님 풀이:

class Transfer:
    def __init__(self, name, account):
        self.name = name
        self.account = account 
        self.balance = 10000
    
    def get_deposit(self, deposit):
        self.balance = self.balance + deposit
        return f'계좌번호: {self.account} / 입금액: {deposit} / 잔액: {self.balance} / {self.name} 고객님 감사합니다.'
    
    def get_withdrawal(self, withdrawal):
        if withdrawal > self.balance:
            return f'{self.name} 고객님 잔액이 부족합니다. 남은
        잔액: {self.balance}원'
        else:
            self.balance = self.balance - withdrawal
            return f'계좌번호: {self.account} / 출금액: {withdrawal} / 잔액: {self.balance} / {self.name} 고객님 감사합니다.'
   
    def __str__(self):
        return f'고객명: {self.name} 계좌명: {self.account} 보유 금액 : {self.balance}'

class Check(Transfer):
    def __init__(self, name, account):
        Transfer.__init__(self, name, account)
    def get_name_cha(self):
        return f'고객명은 {len(self.name)}글자 입니다.'
    def get_balance(self):
        return f'남은 금액: {self.balance}' 

jisun = Check('최지선','110-11')
print(jisun)
print(jisun.get_name_cha())
print(jisun.get_deposit(1000))
print(jisun.get_withdrawal(2000))
print(jisun.get_withdrawal(12000))
print(jisun.get_balance())