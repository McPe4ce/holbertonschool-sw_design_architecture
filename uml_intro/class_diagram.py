#!/usr/bin/env python3
"""Module that creates the library classes after the diagram"""

from __future__ import annotations
from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.catalogue = []
        self.userbase = []

    def add_book(self, *titles):
        for title in titles:
            self.catalogue.append(title)

    def delete_book(self, *titles):
        for title in titles:
            self.catalogue.remove(title)
    
    def register_user(self, *usernames):
        for user in usernames:
            self.userbase.append(user)
        
    def delete_user(self, *usernames):
        for user in usernames:
            self.userbase.remove(user)

    def create_loan(self):
        self.name = input("Name of the user borrowing the book: ")
        self.book = input("Name of the borrowed book: ")
        date_start = input("Borrowed date in (DD/MM): ")
        self.date = datetime.strptime(date_start, "%d/%m")
        returning_date = self.date + timedelta(weeks=2)
        print(f"{self.name} took the {self.book} book on the {self.date.strftime("%d/%m")}")
        print(f"Book must be returned before the {returning_date.strftime("%d/%m")}")

class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email


if __name__ == "__main__":
    bibliotheque = Library()

    """bibliotheque.add_book("Le Rouge et le Noir", "Troie", "Percy Jackson", "Cats")
    print(", ".join(bibliotheque.catalogue))
    bibliotheque.delete_book("Le Rouge et le Noir")
    print(", ".join(bibliotheque.catalogue))
    bibliotheque.register_user("Phil", "Alex", "Charles", "William")
    print(", ".join(bibliotheque.userbase))
    bibliotheque.delete_user("William")
    print(", ".join(bibliotheque.userbase))"""
    bibliotheque.create_loan()