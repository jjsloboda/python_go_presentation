import ctypes
import os

def main():
    path = os.path.join(os.path.abspath("."), "bool_output.so")
    lib = ctypes.CDLL(path)
    print("Answer is: ")
    print("-------------------")
    answer = lib.bool_output()
    print(answer)
    print("-------------------\n\n")

if __name__ == "__main__":
    main()
