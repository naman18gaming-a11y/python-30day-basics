from abc import ABC, abstractmethod

class vechile:
    def start(self):
        pass

class car(vechile):
    def start(self):
        print("cat started")

c = car()
c.start()       