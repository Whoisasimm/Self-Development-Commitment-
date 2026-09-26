"""
DSA DAY 1 — PYTHON + DSA FOUNDATIONS

Topics learned:
- DSA = Data Structures + Algorithms
- Data Structure vs Algorithm
- Problem -> Algorithm -> Python Code -> Output
- Big-O: O(1), O(log n), O(n), O(n^2)
- Python lists, indexing, negative indexing
- Traversal and Linear Search
- Functions: def, parameters, arguments, return
- enumerate() and break
- Two Sum brute force
- Two Pointers introduction
- Sliding Window introduction
"""

# ============================================================
# 1. DSA BASICS
# ============================================================
# Data Structure = how data is organized/stored.
# Algorithm = step-by-step procedure to solve a problem.
#
# Flow:
# PROBLEM -> ALGORITHM -> PYTHON CODE -> OUTPUT


# ============================================================
# 2. BIG-O / TIME COMPLEXITY
# ============================================================
# Time complexity describes how work grows as input size n grows.
#
# O(1)     = constant
# O(log n) = logarithmic
# O(n)     = linear
# O(n^2)   = quadratic

numbers = [10, 20, 30, 40, 50]

# O(1): direct index access
print(numbers[0])

# O(n): visit every element once
for number in numbers:
    print(number)

# O(n^2): two loops that both grow with n
for i in numbers:
    for j in numbers:
        pass

# Two separate O(n) loops are still O(n):
for number in numbers:
    pass

for number in numbers:
    pass

# n + n = 2n -> O(n)
#
# Important trap:
# Nested loops are not automatically O(n^2).
# for i in numbers:
#     for j in range(5):
#         pass
# This is n * 5 = O(n).


# ============================================================
# 3. BINARY SEARCH IDEA
# ============================================================
# Binary Search works on a suitable ordered/sorted search space.
# It repeatedly cuts the search space roughly in half.
#
# Example:
# [10,20,30,40,50,60,70,80], target 70
# check 40 -> restrict right
# check 60 -> restrict right
# check 70 -> found
#
# Binary Search: O(log n)
# Linear Search: O(n) worst case
#
# log2(2)=1, log2(4)=2, log2(8)=3, log2(16)=4.


# ============================================================
# 4. LISTS + INDEXING
# ============================================================
numbers = [10, 20, 30, 40, 50]

# value: 10  20  30  40  50
# index:  0   1   2   3   4

print(numbers[0])  # 10
print(numbers[2])  # 30
print(numbers[4])  # 50

# numbers[5] -> IndexError


# ============================================================
# 5. NEGATIVE INDEXING
# ============================================================
# index:    0   1   2   3   4
# reverse: -5  -4  -3  -2  -1

print(numbers[-1])  # 50
print(numbers[-2])  # 40
print(numbers[-3])  # 30
print(numbers[-5])  # 10

# numbers[-6] -> IndexError


# ============================================================
# 6. TRAVERSAL
# ============================================================
# Traversal = visit elements one by one.
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)

# Visiting n elements once -> O(n)


# ============================================================
# 7. LINEAR SEARCH
# ============================================================
numbers = [7, 12, 25, 31, 46, 50, 63]
target = 50

for number in numbers:
    if number == target:
        print("Found")
        break

# Best case: target is first -> O(1)
# Worst case: target is last/not present -> O(n)


# ============================================================
# 8. FUNCTIONS
# ============================================================
# def = define a function.
# Calling the function executes it.

def square(number):
    return number * number

answer = square(5)
print(answer)  # 25


def cube(number):
    return number * number * number

answer = cube(5)
print(answer)  # 125


# ============================================================
# 9. PARAMETERS vs ARGUMENTS
# ============================================================
def multiply(x, y):
    return x * y

# x and y = PARAMETERS (placeholders)
# 4 and 7 = ARGUMENTS (actual values)

answer = multiply(4, 7)
print(answer)  # 28

# During multiply(4, 7):
# x <- 4
# y <- 7
# x * y -> 4 * 7 -> 28


# ============================================================
# 10. RETURN vs PRINT
# ============================================================
def add(a, b):
    return a + b

result = add(10, 20)
print(result)  # 30

# return sends a value back to the caller.
# print displays something on the screen.


# ============================================================
# 11. enumerate()
# ============================================================
# enumerate() is a Python built-in function.
# It gives index + value while iterating.

numbers = [10, 20, 30]

for index, number in enumerate(numbers):
    print(index, number)

# Output:
# 0 10
# 1 20
# 2 30
#
# "index" is NOT a special Python keyword.
# It is just a variable name chosen by us.


# ============================================================
# 12. LINEAR SEARCH WITH INDEX + break
# ============================================================
numbers = [1, 2, 3, 4, 5]
target = 3

for index, number in enumerate(numbers):
    if number == target:
        print("found", index)
        break
else:
    print("notfound")

# Output: found 2
#
# value: 1  2  3  4  5
# index: 0  1  2  3  4


# ============================================================
# 13. FOR-ELSE
# ============================================================
# A for-loop can have an else.
# The else runs if the loop finishes without break.

numbers = [1, 2, 3, 4, 5]
target = 50

for number in numbers:
    if number == target:
        print("found")
        break
else:
    print("notfound")

# target 50 is absent, so break never happens -> notfound


# ============================================================
# 14. TWO SUM — BRUTE FORCE
# ============================================================
# Problem:
# numbers = [2, 7, 11, 15]
# target = 9
# Find two numbers whose sum is 9.
#
# Brute force checks pairs.
# Two n-sized nested loops -> O(n^2)

numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
            break

# Output: 2 7
#
# i and j are indexes.
# numbers[i] and numbers[j] are the actual values.
#
# Important idea:
# If current = 2 and target = 9:
# needed = target - current = 7


# ============================================================
# 15. ARRAY/LIST OPERATION COMPLEXITIES
# ============================================================
# arr[i]        -> O(1) direct access
# Linear Search -> O(n) worst case
# Append        -> O(1) amortized
# Insert middle -> O(n)
# Delete middle -> O(n)
# Binary Search -> O(log n) when the search space is suitable
#
# Access != Search
# arr[3] is direct access -> O(1)
# finding a value with linear search -> O(n)


# ============================================================
# 16. TWO POINTERS — INTRODUCTION
# ============================================================
# Example:
# [1, 3, 4, 6, 8, 10], target = 10
#
# left = first element
# right = last element
#
# sum < target -> move left rightward
# sum > target -> move right leftward
# sum == target -> found
#
# When ordering lets us safely eliminate search space,
# two pointers can often give O(n).


# ============================================================
# 17. SLIDING WINDOW — INTRODUCTION
# ============================================================
# Example:
# [2, 1, 5, 1, 3, 2]
# Find maximum sum of 3 consecutive elements.
#
# First window: [2,1,5] -> 8
# Slide:
# old sum - outgoing + incoming
# 8 - 2 + 1 = 7
#
# Core idea:
# Maintain a moving contiguous range and reuse previous work.
# This often reduces repeated work and can produce O(n) solutions.


# ============================================================
# DAY 1 CHEAT SHEET
# ============================================================
# DSA = Data Structures + Algorithms
# Data Structure = organization/storage of data
# Algorithm = steps to solve a problem
# Big-O = growth of work with input size
#
# O(1) = constant
# O(log n) = logarithmic
# O(n) = linear
# O(n^2) = quadratic
#
# Python indexing starts at 0.
# -1 = last element.
# Traversal = visit elements one by one.
# Linear Search = check one by one.
# Function = reusable block of logic.
# Parameter = placeholder in function definition.
# Argument = actual value in function call.
# return = sends value back.
# enumerate() = index + value during iteration.
# break = immediately stops loop.
# Two Sum brute force = O(n^2).
# Two Pointers = use two positions and move them by a rule.
# Sliding Window = maintain a moving contiguous range.


# ============================================================
# DAY 1 COMPLETION
# ============================================================
# [x] DSA basics
# [x] Big-O foundations
# [x] Lists/indexing
# [x] Traversal
# [x] Linear Search
# [x] Functions
# [x] Parameters/Arguments
# [x] enumerate()
# [x] break
# [x] Two Sum brute force
# [x] Two Pointers concept
# [x] Sliding Window concept
#
# NEXT SESSION:
# Continue hands-on DSA coding. Understand -> attempt -> hint ->
# manually code -> test -> explain complexity -> variation.
