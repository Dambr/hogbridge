# coding: utf-8

import time

class Timer:
    def __init__(self):
        self.__start = None
        self.__end = None

    def start(self):
        self.__start = time.time()

    def end(self):
        self.__end = time.time()

    def get_duration(self):
        return round(self.__end - self.__start, 2)
