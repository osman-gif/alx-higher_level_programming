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
            summ = add(a, b)
            print("{} + {} = {}".format(a, b, summ))
            exit(0)
        case '-':
            sub = sub(a, b)
            print("{} - {} = {}".format(a, b, sub))
            exit(0)
        case '*':
            mul = mul(a, b)
            print("{} * {} = {}".format(a, b, mul))
            exit(0)
        case '/':
            div = div(a, b)
            print("{} / {} = {}".format(a, b, int(div)))
            exit(0)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
