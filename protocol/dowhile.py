from typing import Optional

def do_while(func, state):
    func()
    while state:
        func()