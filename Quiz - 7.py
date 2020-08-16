#1.입출금 문제
#지선님 풀이:
'''
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
            return f'{self.name} 고객님 잔액이 부족합니다. 남은 잔액: {self.balance}원'
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
'''


#2.자판기 알고리즘
'''
money = int(input('금액을 투입하세요:'))
menu = {'콜라':1000, '핫식스':2000, '환타':500, '커피':3000}
select = ['돈 투입','다른 음료 선택']
vle = list(menu.values())
# print(vle)
# print(menu['콜라'])
cnt = 0
while cnt < 3:
    a = input('메뉴명 입력하세요:')
    if menu[a] <= money:
        money -= menu[a]
        print('{}를 선택했습니다. 남은 잔돈은 {}입니다.'.format(a,money))
        cnt += 1
    elif menu[a] > money:
        print('{}를 선택했습니다. {}만큼 잔돈이 부족합니다.'.format(a,menu[a]-money))
        print("*"*60)
        while True:
            for i, l in enumerate(select, start=1):
                print('{}:{}'.format(i, l))
            sel = int(input('돈을 투입하거나, 다른 음료를 선택해주세요(번호 선택):'))
            print('{}을 선택했습니다'.format(select[sel - 1]))
            if sel == 1:
                add_money = int(input('돈을 투입하세요:'))
                money += add_money
                print('총 잔액은 {}입니다.'.format(money))
            if 0 < sel < 3:
                break
print('3회가 끝났습니다.')
'''

#3. 입국 심사 알고리즘.
# n=6, times = [7, 10](검사관1: 7분, 검사관2:10분)

#첫째, n명의 인원이 랜덤으로 들어간다. 줄은 하나
#두번째, 들어 갈때 무조건 빈자리로 들어간다
#세번째, 들어 가더도 끝나는 시간이 더 적으면 적은 곳으로 들어간다
'''
n = int(input("numbers of people: "))
E = int(input("number of examiners: "))
T = input("time-required for each: ").split()

def logic():
    TR=[]
    i = 0
    if E == len(T):
        
        while i <= n // E:
            i = i+1
            for j in T:
                TR.append(i*int(j))
            TTR = sorted(TR)
        #print(TTR)
        print("it takes about minimum " + str(TTR[n-1]) + "mins for " + str(n) +" people")

    else:
        print("duzn't make sense at all")

logic()
'''
# 각 검사관들의 소요시간을 전부 한 묶음으로 리스트화 한 것이 포인트.
# 문제점은?(맞추기)
# 3명 중 다 같은 경우, 둘만 같은 경우, 전부 다른 
'''
#이분탐색법! BEST!
times = [5, 3, 7] #검사관의 수 및 각자의 검사 시간
n = 500000000 #검사를 받는 사람의 수

mintime = int(min(times) * n / len(times))
maxtime = int(max(times) * n / len(times))
while mintime != maxtime:
    target_time = (mintime + maxtime) // 2
    pass_num = sum([target_time // time for time in times]) - n
    print('min {}, target {}, max {}, pass {}'.format(mintime, target_time, maxtime, pass_num))
    if pass_num >= 0:
        maxtime = target_time
    else:
        mintime = target_time
    if maxtime - mintime == 1:
        break
print(maxtime)
'''

class MyAccount():
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 10000

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return f'계좌번호: {self.account_number} / 입금액: {deposit} / 잔액: {self.balance} / {self.name} 고객님 감사합니다.'

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            return f"{self.name} money lack. current balance is ${self.balance}"
        else:
            self.withdraw = self.balance - withdraw
            return f'account_num: {self.account_number} / withdrawl: {withdraw} / current balance: {self.balance} / {self.name} 고객님 ㄳ.'

    def info(self):
        return f'name: {self.name} account_name: {self.account} current balance: {self.balance}'

class Son(MyAccount):
    def __init__(self, name, account_number):
        MyAccount.__init__(self, name, account_number)
    def name_len(self):
        return f'name is {len(self.name)} numbers of syntaxes'
    def balance(self):
        return f'current balance is {self.balance}'

Jin = Son('김성진','110-1234-5678')
print(Jin.name_len())
print(Jin.deposit(1000))
print(Jin.withdraw(9000))
print(Jin.balance())


#기본틀 of class
'''
class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration

        n = self.data[self.index]
        self.index += 1
        return n

call = MyCollection()
for x in call:
    print(x)
'''

#재귀함수 recursive function 발표
'''
def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
'''
'''
#메모화
dictionary = {1:1, 2:1}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output

print(fibonacci(30))
'''

# Iteration:
def factorial(number):
    product = 1
    for i in range(number):
        product = product * (i+1)
    return product

# Recursion:
def factorial(number):  #base case
    if number <= 1:
        return 1
    else:
        return number*factorial(number-1)




