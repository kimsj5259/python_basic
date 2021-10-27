#1. n나라 (2진수, 8진수, 16진수)
#0 1 2  3  4  5  6   7   8   9   10
#1 2 11 12 21 22 111 112 122 222 1111

'''
def decimal_to_binary(n):
    binary_list = []
    q = 0
    r = 0
    binary_digit = 0
    result = ""
    while True:
        q = int(n/2)
        r = int(n%2)
        binary_digit += 1
        binary_list.append((q,r))
        print("{0} : {1}".format(binary_digit, (q,r)))

        if q != 0:
            n = q
        else:
            break

    for i in range(len(binary_list)):
        result += str(binary_list[-(i+1)][1])
    return(result)

print(decimal_to_binary(10))
'''
#2. 난쟁이 찾기 9명 중 진짜 7명의 합이 100

#3. 첫 주 점수 문제
'''
while True:
    x=[int(x) for x in input("score: ").split()]
    for i in x:
        A = {'age':x[0],'Korean':x[1],'English':x[2],'Math':x[3]}
        print(A)
        return
break
'''
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
    
#4. 신용카드 번호 입력받을때 가운데 8자리를 제외하고 *으로 가려지게.
'''
num = input('card number: ' )
fixed_num = '*' * len(num[4:12])
print(num[0:4], fixed_num, num[12:])
'''

'''
# 정수 입력 -> 2진수, 8진수, 16진수로 출력
#2진수 변환
def BI(x):
    my_list=[]
    while True:
        quo = x // 2
        rem = x % 2
        if rem in range(0,2):
            my_list.insert(0,str(rem)) 
        if quo == 0:
            break
        x = quo
    return ''.join(['0b']+my_list)
#8진수 변환
def OCT(x):
    my_list=[]
    while True:
        quo = x // 8
        rem = x % 8
        if rem in range(0,8):
            my_list.insert(0,str(rem)) 
        if quo == 0:
            break
        x = quo
    return ''.join(['0o']+my_list)
#16진수 변환
def HEX(x):
    my_list=[]
    while True:
        quo = x // 16
        rem = x % 16
        if rem in range(1,10):
            my_list.insert(0,str(rem)) 
        elif rem in range(10,16):
            my_list.insert(0,chr(rem+55)) #chr:숫자에 해당하는 아스키코드(문자)출력
        if quo == 0:                      #ord:문자에 해당하는 아스키코드(숫자)출력
            break
        x = quo
    return ''.join(['0x']+my_list)
#main 코드
num = int(input('숫자를 입력 하세요.: '))
print('{}\n{}\n{}'.format(BI(num),OCT(num),HEX(num)))
'''
# str형태로 리스트에 넣은 이유: join이 int형태는 합쳐주지 못 해서
'''
def amazing_function(number, r):
    number_front = int(number)
    number_rear = number - number_front
    remainder_list = []

    while True:
        quotient = divmod(number_front, r)[0]
        remainder = divmod(number_front, r)[1]

        remainder_list.append(remainder)

        if quotient == 0:
            break
        else:
            number_front = quotient

    remainder_list.reverse()

    result_front = ""
    for digit in remainder_list:
        result_front += str(digit)

    integer_part_list = []

    while True:
        integer_part = int(number_rear * r)
        decimal_part = number_rear*r - integer_part
        integer_part_list.append(integer_part)
        if decimal_part == 0:
            break
        else:
            number_rear = decimal_part

        result_rear =""
        for digit in integer_part_list:
            result_rear += str(digit)

        result = result_front + "." + result_rear
        return result

print(decimal_to_r_notation(10, 16))
'''
'''
hex1 = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
integer = int(input("any: "))
print(str(hex1[integer//16])+str(hex1[integer%16]))

bi = [0,1] #10,11,100,101,111,1000,1001,1011,1111,10000
integer = int(input("num: "))
print(str(bi[integer//2]) + str(bi[integer%2]))
'''

'''
hex1 = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
def to_hex(n):
    result = ""
    if n == 0:
        return '0'
    while n != 0:
        result += str(hex1[(n % 16)])
        n = n // 16
    return '0x'+result[::-1]
print(to_hex(16))
'''
'''
def bin1(n):
    if n > 1:
        bin1(n//2)
    print( n % 2, end='')
num = 10
bin1(num)
print()

def bin1(n):
    if n > 1:
        bin1(n//2)
    print(n%2, end='')
bin1(n=5)
'''
'''
def oct1(n):
    if n > 1:
        oct1(n // 8)
    print(n % 8, end='')
oct1(n=4)
'''


# 몫과 나머지
'''
lights = [6,2,5,5,4,5,6,3,7,6]

memo = {}
def lights_num(number):
    if number in memo: return memo[number]
    output = 0 #02
    for i in "{:02}".format(number):
        output += lights[int(i)]

    memo[number] = output
    return output

cnt = 0
for h in range(0, 24):
    for m in range(0, 60):
        for s in range(0, 60):
            if lights_num(h) + lights_num(m) + lights_num(s) == 30:
                cnt += 1
print(cnt)
'''
'''
def bin1(n):
    prev=''
    if n > 1:
        prev = bin1(n//2)
    return prev + str(n%2)
print(bin1(n=30))

def oct1(n):
    prev=''
    if n > 1:
        prev = oct1(n//8)
    return prev + str(n%8)
print(oct1(n=300))

def hex1(n):
    prev=''
    if n > 1:
        prev = hex1(n//16)
    return prev + str(n%16)
print(hex1(n=501))
'''
'''
a =sorted(dwarf,key= lambda i : dwarf[i])
for x in a:
     print('{}: {}'.format(x,dwarf[x]))

#난쟁이 1~9까지 키 값 부여
import random
def setting(my_list):
    my_dict={}
    n = 1
    for i in my_list:
        my_dict['난쟁이{}'.format(n)] = i
        n +=1
    return my_dict
#dict key와 value 값 뒤집기
def rev (my_list):
    revers = {a:b for b,a in my_list.items()}
    return revers
x=[int(i) for i in input("난쟁이들의 키를 입력하세요.: ").split()]
dwarf = setting(x)
r_dwarf = rev(dwarf)
dwarf_key = list(dwarf.keys())
dwarf_val = list(dwarf.values())
#오름차순 출력
# dwarf_val.sort()
# for i in dwarf_val:
#     if i in r_dwarf:
#         print(‘{}: {}‘.format(r_dwarf[i],i))
a =sorted(dwarf,key= lambda i : dwarf[i])
for x in a:
     print('{}: {}'.format(x,dwarf[x]))
'''
