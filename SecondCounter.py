import threading
import sys
import time

class SecondCounter(threading.Thread):
    def __init__(self, interval=0.001):
        threading.Thread.__init__(self)
        self.interval = interval
        self.value = 0
        self.alive = False

    def run(self):
        self.alive = True
        while self.alive:
            time.sleep(self.interval)
            self.value += self.interval

    def peek(self):
        return self.value

    def finish(self):
        self.alive = False
        return self.value

count = SecondCounter()

count.start()

e = input('Press Enter.')
e = input('Press Enter Again.')

seconds = count.finish()

print('You took {} seconds between Enter actions'.format(seconds))