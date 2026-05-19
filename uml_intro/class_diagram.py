#!/usr/bin/env python3
"""Module that creates the library classes after the diagram"""

from __future__ import annotations

class Library:
    catalogue = []

    def add_book(self, title):
        self.catalogue.append(title)


if __name__ == "__main__":
    bibliotheque = Library()

    bibliotheque.add_book("Le Rouge et le Noir")
    print(Library.catalogue)