import subprocess
import argparse

def f1():
    print("function 1")
def f2():
    print("function 2")
def f3():
    print("function 3")

functions = [f1, f2, f3]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cases", nargs='+', type=int)
    args = parser.parse_args()

    if len(args.cases) > 1:
        for c in args.cases:
            subprocess.call(["python", __file__, f"{c}"])
    else:
        case = args.cases[0]
        functions[case]()

if __name__ == '__main__':
    main()
