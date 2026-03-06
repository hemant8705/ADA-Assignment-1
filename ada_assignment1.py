•	TASK 1: Algorithm Growth Observation
1.	Constant Time {O(1)}:

import time

start_time = time.time()

n = 10
result = n + n
print(result)

end_time = time.time()
print

2.Linear Time {O(n)}:

import time

start_time = time.time()

n = 1000
total = 0

for i in range(n):
    total += i

print(total)

end_time = time.time()

print("Execution Time:", end_time - start_time)

3.Quadratic Time{ O(n^2)}:

import time

start_time = time.time()

n = 300
count = n * n

print(count)

end_time = time.time()
print("Execution Time:", end_time - start_time)

4.Logarithmic Time{ O(logn)}:

import time

start_time = time.time()

n = 1000
count = 0
i = 2

while i <= n:
    i = i * 2
    count += 1

print(count)

end_time = time.time()
print("Execution Time:", end_time - start_time)

TASK 2: Best, Average, and Worst Case Analysis
Linear Search:
•	Best Case:

import time

arr = list(range(1, 1001))
key = 1

start_time = time.time()

index = arr.index(key)

end_time = time.time()

print("Best Case Time:", end_time - start_time)

•	Average Case:

import time

arr = [5, 10, 15, 20, 25]
key = 15

start_time = time.time()

found = False
for i in range(len(arr)):
    if arr[i] == key:
        found = True
        position = i
        break

end_time = time.time()

print("Average Case Time:", end_time - start_time)


Worst Case:

import time

arr = [5, 10, 15, 20, 25]
key = 125

start_time = time.time()

i = 0
while i < len(arr):
    if arr[i] == key:
        break
    i += 1

end_time = time.time()

print("Worst Case Time:", end_time - start_time)

TASK 3: Recursion and Recurrence Validation
•	FACTORIAL:

import time

start_time = time.time()

n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)

end_time = time.time()
print("Execution Time:", end_time - start_time)

•	FIBONACCI(RECURSIVE):

import time

start_time = time.time()

n = 6
a, b = 0, 1

for i in range(n):
    a, b = b, a + b

print("Fibonacci:", a)

end_time = time.time()
print("Execution Time:", end_time - start_time)

•	FIBONACCI(ITERATIVE):

import time

start_time = time.time()

n = 6
a = 0
b = 1

print("Fibonacci Series:")

i = 0
while i < n:
    print(a)
    temp = a + b
    a = b
    b = temp
    i += 1

end_time = time.time()

print("Execution Time:", end_time - start_time)

TASK 4: SOLVING RECURRENCES THROUGH CODE

import time

def rec1(n, calls):
    calls += 1
    if n <= 1:
        return 1, calls
    result, calls = rec1(n // 2, calls)
    return result + n, calls

print("n | Calls | Execution Time")

for n in [8, 16, 32, 64]:
    start = time.time()
    result, calls = rec1(n, 0)
    end = time.time()
    
    print(n, "|", calls, "|", end - start)

2.	T(n) = 2T(n/2) + n

import time

def rec2(n, calls):
    calls += 1
    if n <= 1:
        return 1, calls
    result, calls = rec2(n // 2, calls)
    return 2 * result + n, calls

print("n | Calls | Execution Time")

for n in [8, 16, 32, 64]:
    start = time.time()
    result, calls = rec2(n, 0)
    end = time.time()
    
    print(n, "|", calls, "|", end - start)
