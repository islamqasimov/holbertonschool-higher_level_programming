#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    if arg_len == 0:
        print(f"{arg_len} arguments.")
    else:
        print(f"{arg_len} arguments:")
        for i, arg in enumerate(sys.argv[1:]):
            print(f"{i+1}: {arg}")
