# Exercise 1
import torch
import torch.nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total

class MyStableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x, dim=0)
        x_exp = torch.exp(x - c.values)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


# Exercise 2
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, yob):
        self.__name = name
        self.__yob = yob

    def get_name(self):
        return self.__name

    def get_yob(self):
        return self.__yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(f"Student - Name: {self.get_name()} - YoB: {self.get_yob()} - Grade: {self.__grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(f"Teacher - Name: {self.get_name()} - YoB: {self.get_yob()} - Subject: {self.__subject}")

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self.get_name()} - YoB: {self.get_yob()} - Specialist: {self.__specialist}")

class Ward:
    def __init__(self, name):
        self.__name = name
        self.__person_list = []

    def add_person(self, person: Person):
        self.__person_list.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__person_list:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.__person_list if isinstance(person, Doctor))

    def sort_age(self):
        self.__person_list.sort(key=lambda person: person.get_yob())

    def compute_average(self):
        teachers = [person for person in self.__person_list if isinstance(person, Teacher)]
        if not teachers:
            return 0 
        total_age = sum(teacher.get_yob() for teacher in teachers)
        return total_age / len(teachers)

# Exercise 3
class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__list_stack = []

    def is_empty(self):
        return len(self.__list_stack) == 0

    def is_full(self):
        return len(self.__list_stack) == self.__capacity

    def pop(self):
        if not self.is_empty():
            return self.__list_stack.pop()
        return None

    def push(self, value):
        if not self.is_full():
            self.__list_stack.append(value)

    def top(self):
        if not self.is_empty():
            return self.__list_stack[-1]
        return None

# Exercise 4
class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__list_queue = []

    def is_empty(self):
        return len(self.__list_queue) == 0

    def is_full(self):
        return len(self.__list_queue) == self.__capacity

    def dequeue(self):
        if not self.is_empty():
            return self.__list_queue.pop(0)
        return None

    def enqueue(self, value):
        if not self.is_full():
            self.__list_queue.append(value)

    def front(self):
        if not self.is_empty():
            return self.__list_queue[0]
        return None

