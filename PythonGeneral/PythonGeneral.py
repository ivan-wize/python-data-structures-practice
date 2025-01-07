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

# 1. Write a Python script to parse and validate JSON data from an API response.
# 2. Create a function that detects memory leaks in a continuous data stream.
# 3. Develop a Python script to automate testing of firmware update processes.
# 4. Implement a function to simulate a network outage and recover a device.
# 5. Write code to generate test logs, handle failures, and send email reports.

### Final Notes
# Practice these patterns on LeetCode, especially focusing on:
# - Sliding Window Problems
# - Dynamic Programming (Fibonacci, Knapsack)
# - Graph Algorithms (DFS, BFS, Dijkstra)
# - Recursion and Backtracking (N-Queens, Subsets)
# - Binary Search (Search Rotated Sorted Array)
