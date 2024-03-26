#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:08:33 2024

@author: maritaolano
"""
# Assignment 06 
# Question 4: Library Management System 

# base class 
class LibraryItem:
    def __init__(self, title, subject, location):
        self.title = title
        self.subject = subject 
        self.location = location 
        self.checked_out_1 = False 
    # abstract method checked out 
    def check_out(self):
        if not self.checked_out_1: # if True (not False) then print 
            print(f"{self.title} successfully checked out")
        else: # if False
            print(f"{self.title} is already checked out")
    # abstract method return item
    def return_item(self):
        if self.checked_out_1: # if False then print
            print(f"{self.title} successfully returned")
        else: # if True 
            print(f"{self.title} is not checked out")
    # to print details of the item 
    def get_details(self):
        print(f"Title: {self.title}")
        print(f"Subject: {self.subject}")
        print(f"Location: {self.location}")
        print(f"Status: Checked Out" if self.checked_out_1 else "Available")
        
class Book(LibraryItem):
    def __init__(self, title, subject, location, author, ISBN):
        super().__init__(title, subject, location)
        self.author = author
        self.ISBN = ISBN
        
class DVD(LibraryItem):
    def __init__(self, title, subject, location, director, genre, run_time):
        super().__init__(title, subject, location)
        self.genre = genre
        self.run_time = run_time
        
class Journal(LibraryItem):
    def __init__(self, title, subject, location, volume, issue_number):
        super().__init__(title, subject, location)
        self.volume = volume
        self.issue_number = issue_number
    

class LibraryCatalog:
    def __init__(self):
        self.catalog = []

    # to add a new item to the catalog
    def add_item(self, item):
        self.catalog.append(item)
        print(f"{item.title} added to the catalog")
        
    # to remove an item from the catalog     
    def remove_item(self, title):
        for item in self.catalog:
            if item.title == title:
                self.catalog.remove(item)
                print(f"{item.title} removed from the catalog")
                return
        print(f"{title} not found in the catalog")
    
    # searchs for an iteam by title and returns it 
    def find_item_by_title(self, title):
        for item in self.catalog:
            if item.title == title:
                print(f"{title} is in the catalog")
                True
                break
        else:
            print(f"{title} not found in the catalog")

    # checks out an item by calling check_out() method
    def check_out_item(self, title):
        for item in self.catalog:
            if item.title == title:
                item.check_out()
                return
        print(f"{title} not found in the catalog")
        
    # returns an item by calling return_item() method
    def return_item(self, title):
        for item in self.catalog:
            if item.title == title:
                item.return_item()
                return
        print(f"{title} not found in the catalog")

def main():
    catalog = LibraryCatalog()
    
    # to add item to catalog
    book_1 = Book("Dune", "Science Fiction", "SF", "Frank Herbert", 1234)
    catalog.add_item(book_1)
    dvd_1 = DVD("Barbie", "Fantasy", "DVD", "Greta Gerwig", "Comedy", 9876)
    catalog.add_item(dvd_1)
    journal_1 = Journal("NYT", "Science", "Journals", "2023", "March")
    catalog.add_item(journal_1)
    
    # to find item by title
    catalog.find_item_by_title("\nDune")
    catalog.find_item_by_title("Dune 2")
    
    # Checking out items
    catalog.check_out_item("\nDune")
    catalog.check_out_item("Barbie")
    catalog.check_out_item("NYT")
    
    # Returning items
    catalog.return_item("\nDune")
    catalog.return_item("Barbie")
    catalog.return_item("NYT")
    
    # to remove an item
    catalog.remove_item("\nNYT")
    print("\n")
    
    # to get details of an item
    book_1.get_details()
    
main() 