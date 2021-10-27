# List Comprehension
'''
new_list = [ x for x in range(1, 11) ]
print(new_list)
'''
#if문을 포함하는 리스트 컴프리헨션 형식
'''
odd_numbers = [ ]
for element in range(1,11):
    if (element % 2) == 1:
        odd_numbers.append(element)
'''
# if문을 포함하는 리스트 컴프리헨션으로 위의 4줄을 한줄로:
'''
list_comprehension = [element for element in range(1,11) if (element % 2) == 1]
print(list_comprehension)
'''
# timeit모듈을 사용하여 함수들을 1000번 실행한 시간을 측정하는 코드 입니다.
# for vs list comprehension
'''
import timeit

def for_loop():
num_list = []
for i in range(1000):
num_list.append(i)

def list_comprehension():
num_list = [ i for i in range(1000) ]

if __name__ == "__main__":
time1 = timeit.Timer("for_loop()", "from __main__ import for_loop")
print("for loop time = ", time1.timeit(number=1000), "milliseconds")

time2 = timeit.Timer("list_comprehension()", "from __main__ import list_comprehension")
print("list_comprehension time = ", time2.timeit(number=1000), "milliseconds")
'''

# list comprehension Assignment1
cities = ["Tokyo", "Shanghai", "Jakarta", "Seoul", "Guangzhou", "Beijing",
         "Karachi", "Shenzhen", "Delhi" ]
#for loop
'''
lists = []
for element in cities:
    temp_list = list(element)
    if temp_list[0] != "S":
        lists.append(element)
print(lists)

list_cities = [ element for element in cities if "S" not in element ]
print(list_cities)
'''
# list comprehension Assignment2
population_of_city = [('Tokyo', 36923000), ('Shanghai', 34000000),
                      ('Jakarta', 30000000), ('Seoul', 25514000),
                      ('Guangzhou', 25000000), ('Beijing', 24900000),
                      ('Karachi', 24300000 ), ('Shenzhen', 23300000),
                      ('Delhi', 21753486) ]

dict_city = {i:j for i ,j in population_of_city}
print(dict_city)

print(dict(population_of_city))

