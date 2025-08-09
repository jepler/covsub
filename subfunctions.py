import subprocess
import argparse

# (Gets coverage of the non-taken if branch)
import subfunctions
assert subfunctions.__name__ == 'subfunctions'

import randsleep

def f0():
    print("function 0")


def f1():
    print("function 1")


def f2():
    print("function 2")


def f3():
    print("function 3")


def f4():
    print("function 4")


def f5():
    print("function 5")


def f6():
    print("function 6")


def f7():
    print("function 7")


def f8():
    print("function 8")


def f9():
    print("function 9")


def f10():
    print("function 10")


def f11():
    print("function 11")


def f12():
    print("function 12")


def f13():
    print("function 13")


def f14():
    print("function 14")


def f15():
    print("function 15")


def f16():
    print("function 16")


def f17():
    print("function 17")


def f18():
    print("function 18")


def f19():
    print("function 19")


def f20():
    print("function 20")


def f21():
    print("function 21")


def f22():
    print("function 22")


def f23():
    print("function 23")


def f24():
    print("function 24")


def f25():
    print("function 25")


def f26():
    print("function 26")


def f27():
    print("function 27")


def f28():
    print("function 28")


def f29():
    print("function 29")


def f30():
    print("function 30")


def f31():
    print("function 31")


def f32():
    print("function 32")


def f33():
    print("function 33")


def f34():
    print("function 34")


def f35():
    print("function 35")


def f36():
    print("function 36")


def f37():
    print("function 37")


def f38():
    print("function 38")


def f39():
    print("function 39")


def f40():
    print("function 40")


def f41():
    print("function 41")


def f42():
    print("function 42")


def f43():
    print("function 43")


def f44():
    print("function 44")


def f45():
    print("function 45")


def f46():
    print("function 46")


def f47():
    print("function 47")


def f48():
    print("function 48")


def f49():
    print("function 49")


def f50():
    print("function 50")


def f51():
    print("function 51")


def f52():
    print("function 52")


def f53():
    print("function 53")


def f54():
    print("function 54")


def f55():
    print("function 55")


def f56():
    print("function 56")


def f57():
    print("function 57")


def f58():
    print("function 58")


def f59():
    print("function 59")


def f60():
    print("function 60")


def f61():
    print("function 61")


def f62():
    print("function 62")


def f63():
    print("function 63")


def f64():
    print("function 64")


def f65():
    print("function 65")


def f66():
    print("function 66")


def f67():
    print("function 67")


def f68():
    print("function 68")


def f69():
    print("function 69")


def f70():
    print("function 70")


def f71():
    print("function 71")


def f72():
    print("function 72")


def f73():
    print("function 73")


def f74():
    print("function 74")


def f75():
    print("function 75")


def f76():
    print("function 76")


def f77():
    print("function 77")


def f78():
    print("function 78")


def f79():
    print("function 79")


def f80():
    print("function 80")


def f81():
    print("function 81")


def f82():
    print("function 82")


def f83():
    print("function 83")


def f84():
    print("function 84")


def f85():
    print("function 85")


def f86():
    print("function 86")


def f87():
    print("function 87")


def f88():
    print("function 88")


def f89():
    print("function 89")


def f90():
    print("function 90")


def f91():
    print("function 91")


def f92():
    print("function 92")


def f93():
    print("function 93")


def f94():
    print("function 94")


def f95():
    print("function 95")


def f96():
    print("function 96")


def f97():
    print("function 97")


def f98():
    print("function 98")


def f99():
    print("function 99")


functions = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65,f66,f67,f68,f69,f70,f71,f72,f73,f74,f75,f76,f77,f78,f79,f80,f81,f82,f83,f84,f85,f86,f87,f88,f89,f90,f91,f92,f93,f94,f95,f96,f97,f98,f99]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int, default=len(functions))
    args = parser.parse_args()
    
    cases = list(range(args.start, args.stop))
    if len(cases) > 1:
        for c in cases:
            subprocess.call(["python", __file__, f"--start={c}", f"--stop={c+1}"])
    else:
        randsleep.randsleep()
        case = cases[0]
        functions[case]()

if __name__ == '__main__':
    main()
