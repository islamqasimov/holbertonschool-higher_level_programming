#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    all_args = [f"{i+1}: {arg}" for i, arg in enumerate(sys.argv[1:])]
    if arg_len == 0:
        print(f"{arg_len} arguments.")
    elif arg_len == 1:
        print(f"{arg_len} argument:")
        print(all_args[0])
    else:
        print(f"{arg_len} arguments:")
        print("\n".join(all_args))
