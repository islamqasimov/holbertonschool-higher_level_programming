#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    all_args = [int(num) for num in sys.argv[1:]]
    print(sum(all_args))
