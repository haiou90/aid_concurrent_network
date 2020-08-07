#!/usr/bin/python3

result = 1

for i in range(1,101):
    if i % 2 != 0:
        result *= i 

print(result) 


result = 1 

for i in [x for x in range(1,101,2)]:
    result *= i 

print(result)
