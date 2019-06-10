import sys
from generator import main


def init():
    args = sys.argv
    main.execute(args)


if __name__ == '__main__':
    init()
