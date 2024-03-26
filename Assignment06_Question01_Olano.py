#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:48:28 2024

@author: maritaolano
"""

# Assignment 06 
# Question 1: Animal Kingdom Hierarchy 

# base class 
class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

# derived classes mammal, bird, fish 
class Mammal(Animal):
    def give_birth(self):
        print("Mammal is drinking milk")

class Bird(Animal):
    def fly(self):
        print("Bird is flying")

class Fish(Animal):
    def swim(self):
        print("Fish is swimming")


# derived specific animal classes 
class Dog(Mammal):
    def eat(self): # override base class methods to perform actions specific to that animal
        print("Dog is eating")
    def bark(self):
        print("Dog is barking")

class Eagle(Bird):
    def eat(self):
        print("Eagle is eating")

    def hunt(self):
        print("Eagle is hunting")
        
class Flying_Fish(Fish):
    def swim(self):
        print("Flying Fish is swimming")

    def fly(self):
        print("Flying Fish is flying")        


# to demonstrate polymorphism
def function_1(animal):
    animal.eat()


def main():
    dog = Dog()
    flying_fish = Flying_Fish()
    eagle = Eagle()
    
    # Dog 
    dog.eat()  
    dog.sleep()  
    dog.bark()  
    dog.give_birth()  
    
    # Flying Fish 
    print("\n")
    flying_fish.eat() 
    flying_fish.sleep()  
    flying_fish.swim()  
    flying_fish.fly()  
    
    # Eagle 
    print("\n")
    eagle.eat()  
    eagle.sleep()  
    eagle.fly()  
    eagle.hunt()  
    
    # to demostrate polymorphism 
    print("\n")
    function_1(dog)  
    function_1(flying_fish) 
    function_1(eagle) 

main()