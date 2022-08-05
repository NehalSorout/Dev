# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from lib.base import addition
import os
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(addition(4, 6))
    print(addition('4', '5'))
    print(addition(ord('4'), 0))
    print(os.environ["CONSUMER"])
    print(os.getcwd())