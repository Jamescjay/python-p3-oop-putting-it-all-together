#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title

        if not isinstance(page_count, int):
            print("page_count must be an integer")
            return 

        self.page_count = page_count
        self.current_page = 1

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        self.current_page += 1
