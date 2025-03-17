# Python Cheat Sheet for Apple Interview Preparation

### 1. Common Built-in Functions

# List operations
nums = [1, 2, 3, 4, 5]
nums.append(6)          # Add to end
nums.insert(2, 99)      # Insert at index 2
nums.remove(3)          # Remove first occurrence
nums.pop()              # Remove and return last element
nums.sort(reverse=True) # Sort in descending order
nums.reverse()          # Reverse the list

# String operations
text = "hello world"
text.upper()            # Uppercase
text.lower()            # Lowercase
text.title()            # Title case
text.split()            # Split into list
text.strip()            # Remove leading/trailing spaces
text.replace('world', 'Apple') # Replace substrings

# Dictionary operations
data = {"name": "Ivan", "age": 36}
data.keys()             # Get keys
data.values()           # Get values
data.items()            # Get key-value pairs
data.get("name")        # Get value by key
data.update({"job": "QA"}) # Update with new key-value pairs

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.union(set2)        # Combine sets
set1.intersection(set2) # Find common elements
set1.difference(set2)   # Find elements only in set1

### 2. Common Algorithms & Patterns

# Two Sum
nums = [2, 7, 11, 15]
target = 9
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# Valid Parenthesis
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

# Group Anagrams
def group_anagrams(strs):
    from collections import defaultdict
    ans = defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return list(ans.values())

# Maximum Subarray
def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Spiral Matrix
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

# Best Time to Buy and Sell Stock
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

# Reverse Integer
def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10
    result *= sign
    return result if -2**31 <= result <= 2**31 - 1 else 0

# Single Number
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Longest Common Prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Reverse String
s = "apple"
print(s[::-1])

# Fibonacci (Dynamic Programming)
def fib(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

### 3. Object-Oriented Programming (OOP) Best Practices

# Class with Encapsulation
# Class with Encapsulation - Demonstrates encapsulation by keeping attributes private and providing getter and setter methods
class Employee:
    def __init__(self, name, salary):
        self.__name = name            # Private attribute
        self.__salary = salary        # Private attribute

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Salary must be positive")

# Inheritance
# Inheritance - Demonstrates inheritance, where Manager inherits properties and methods from Employee
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_team_size(self):
        return self.team_size

# Polymorphism
# Polymorphism - Demonstrates polymorphism by defining a base class method that is overridden in subclasses
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Abstract Class
from abc import ABC, abstractmethod
# Abstract Class - Demonstrates abstraction using an abstract base class to enforce implementation of the 'area' method in subclasses
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

### 4. Error Handling

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors encountered.")
finally:
    print("Execution completed.")

### 5. Useful Python Modules

import os
os.listdir('.')           # List files in directory
os.path.exists('file.txt') # Check if file exists

import sys
print(sys.version)         # Print Python version

import datetime
print(datetime.datetime.now()) # Get current date and time

import collections
counter = collections.Counter([1, 2, 2, 3, 3, 3])
print(counter)             # Frequency count

import itertools
perms = list(itertools.permutations([1, 2, 3]))
print(perms)               # Generate permutations

import heapq
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
print(heapq.heappop(heap)) # Min-heap operation

### 6. Tips for Optimization

# Use List Comprehensions
squared = [x**2 for x in range(10)]

# Use Generators for Memory Efficiency
def generator_example():
    for i in range(10):
        yield i

# Avoid Deep Nesting (Use Guard Clauses)
def process_data(data):
    if not data:
        return None
    return [d.upper() for d in data if isinstance(d, str)]

### 7. Pythonic Tricks

# Swap Values
a, b = 1, 2
a, b = b, a

# Merge Dictionaries
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}

# Flatten a List
nested = [[1, 2], [3, 4]]
flat = [item for sublist in nested for item in sublist]

# Lambda Functions
square = lambda x: x ** 2
print(square(4))

### 8. Sample Interview Problems for QA Automation Role

# 1. Parse and Validate JSON data from an API response
import json
response = '{"status": 200, "message": "OK"}'
try:
    data = json.loads(response)
    assert "status" in data and "message" in data
    print("JSON is valid.")
except Exception as e:
    print(f"Invalid JSON: {e}")

# 2. Detect Memory Leaks in Continuous Data Stream
def detect_memory_leak(data_stream):
    seen = set()
    for data in data_stream:
        if data in seen:
            return True  # Memory leak detected
        seen.add(data)
    return False

# 3. Automate Firmware Update Process
import subprocess
try:
    result = subprocess.run(["firmware_update.sh"], check=True)
    print("Firmware update successful.")
except subprocess.CalledProcessError:
    print("Firmware update failed.")

# 4. Simulate Network Outage and Recover Device
import time
import os

def simulate_outage():
    os.system("sudo ifconfig eth0 down")  # Disable network
    time.sleep(10)
    os.system("sudo ifconfig eth0 up")  # Enable network

# 5. Generate Test Logs, Handle Failures, Send Email Reports
import logging
import smtplib

logging.basicConfig(filename='test.log', level=logging.INFO)
try:
    logging.info("Test started.")
    # Simulate test
    assert 1 == 1
    logging.info("Test passed.")
except AssertionError:
    logging.error("Test failed.")
    with smtplib.SMTP("smtp.example.com") as server:
        server.sendmail("from@example.com", "to@example.com", "Test failed.")
finally:
    logging.info("Test completed.")
