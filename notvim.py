import os, sys


def text_area(filename, file_text):
    file_text = input("")




if __name__ == "__main__":
    args = sys.args
    if args[1]:
        try:
            f = open(args[1])
            text_area(args[1], f)
    text_area(sys.argv[1]):
