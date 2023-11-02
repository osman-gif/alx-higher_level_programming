#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, mul, div, sub
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = str(sys.argv[2])

    match op:
        case '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            exit(0)
        case '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            exit(0)
        case '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            exit(0)
        case '/':
            print("{} / {} = {}".format(a, b, int(div(a, b))))
            exit(0)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
