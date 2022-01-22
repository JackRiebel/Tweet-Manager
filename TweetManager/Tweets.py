import time
import math

class Tweet:
    # Define what happens when a new tweet is created
    def __init__(self, author, text, age):
        self.__author = author
        self.__text = text
        self.__age = age

    # Return the tweets author
    def get_author(self):
        return self.__author

    # Return the tweets text
    def get_text(self):
        return self.__text

    # Return the tweets age
    def get_age(self):
        now = time.time()
        elapsed = now - self.__age

        return math.floor(elapsed)
