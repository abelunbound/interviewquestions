import sys
import time


def write(text, speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        time.sleep(speed)

    print("")  # flush a line

name = input("Would you be kind enough to tell me your name?\n")
write(name, speed=0.02)