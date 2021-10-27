# Python Quiz 4

#1.백설공주와 아홉난쟁이 중 진짜 일곱난쟁이(진짜 일곱의 합=100)
'''
import random

height = [x for x in range(100) and x<93]
dwarf = random.sample(height, 7)
sum_dwarf = sum(dwarf)
print(sum_dwarf)

while True:
    if sum_dwarf <100:
        dwarf = random.sample(height, 7)
        sum_dwarf = sum(dwarf)
        print(sum_dwarf)
'''

'''
import random
L = [random.randint(1, 101) for _ in range(7)]
print(L)    
'''    
    
'''
height=[]

for dwarf in range(9):
    height.append(int(input()))
sum1=sum(height)

height.sort()
for dwarf in range(9):
    for fake in range(dwarf+1, 9):
        if sum1-height[dwarf]-height[dwarf] == 100:
            for real in range(9):
                if real==dwarf or real==fake: continue
                else:
                    print(height[real])

'''

#2.남녀 파트너를 정해주는 코드
'''
from random import shuffle

male = ['슈퍼맨', '심봉사', '로미오', '이몽룡', '마루치']
female = ['원더우먼', '뺑덕', '줄리엣', '성춘향', '아라치']
shuffle(male)
shuffle(female)

couples = zip(male, female)

for i, couple in enumerate(couples):
    print(f'커플{i+1}:{couple[0]}-{couple[1]}')

import random
male = ['슈퍼맨', '심봉사', '로미오', '이몽룡', '마루치']
female = ['원더우먼', '뺑덕', '줄리엣', '성춘향', '아라치']

n = male + female
random.shuffle(n)
while len(n) != 0:
    v = n.pop()
    w = n.pop()
    print(v,w)
'''
#3.숫자들이 들어있는 배열 num에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 구하시오.
'''
def prime_number(number): #number를 입력 받아 소수인지 아닌지 구분하는 함수
    if number != 1: #number가 1이 아니면, (1은 소수가 아님)
        #2, 3, 4, ..., (number - 1)까지의 인수에 대해서
        for f in range(2, number):
            #number가 위의 인수 중의 하나로 나누어지면, (나머지가 0이면)
            if number % f == 0:
                return False    #소수가 아님
                       
    return True            #소수가 아님

    #number가 1이 아니면서, 2부터 (number - 1)까지의 수로 나눠지지 않으므로
    #소수로 판별됨 (소수는 1과 자신만을 인수로 갖는 수)

import random

a = [x for x in range(5)]
b = random.sample(a, 3)
c = sum(b)

print(b)
print(c)
if prime_number(c):
    print("Sum of them is" + str(c) + " a prime number.")
else:
    print("Sum of them is" + str(c) + " Not a prime number.")
'''
'''
def prime_number(number): #1
    if number == 1:
        return False
 
    else:
        i = 2 
        j = number
        while i <= j:
            if i == number:
                return True
            elif number % i == 0:
                return False
            else:
                j = number // i
                i += 1
 
        return True
 
def get_number_of_prime_numbers_for_sum_of_three(): #2
    result = 0 
    for i in range(1, 1001):
        if prime_number(i): #포함1
            result += 1
 
    return result
 
print(get_number_of_prime_numbers_for_sum_of_three())
'''
#4.알파벳 소문자로 문자열 출력 프로그램
'''
def solution(s):
    start = 0
    while start < len(s) - 1: 
        if s[start] == s[start+1]:
            s = s[0:start] + s[start+2:];
            start = max(0, start-1)
        else:
            start += 1
    if len(s) == 0:
        return 1
    else:
        return 0
print(solution(input("alphabet: ")))
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


#5.문자 입력해서 앞과 끝이 같은지
'''
word = input('word: ')

is_palindrome = True            #초기값
for i in range(len(word) // 2): #비교할 때 반으로 나눠서 하나씩
    if word[i] != word[-1 - i]: #[0]과 [-1], [1]과[-2] 등등비교
        is_palindrome = False   #회문 아니니까 False
        break              
    
print(is_palindrome)


import itertools #경우의 수를 뽑아주는 모듈

num =[int(n) for n in input('1000이하의 자연수를 중복 없이 3~50개 입력하세요.:').split()]
case = list(itertools.combinations(num,3))#순서 상관없음, 중복x
count = 0
for i in case:
    a = sum(i)
    div = []
    for x in range(1,a+1):
        if a % x == 0:
            div.append(x)
    if len(div) == 2:
        print(div[1],i)
        count += 1
print('입력한 수들에서 3개를 뽑아 더했을 때 소수가 되는 경우의 수 :',count)
'''

