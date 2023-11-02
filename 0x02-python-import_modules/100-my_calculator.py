#!/usr/bin/python3
import sys
import calculator_1 as cal

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
op = sys.argv[2]

match op:
    case '+':
        summ = cal.add(a, b)
        print("{} + {} = {}".format(a, b, summ))
    case '-':
        sub = cal.sub(a, b)
        print("{} - {} = {}".format(a, b, sub))
    case '*':
        mul = cal.mul(a, b)
        print("{} * {} = {}".format(a, b, mul))
    case '/':
        div = cal.div(a, b)
        print("{} / {} = {}".format(a, b, int(div)))

if __name__ == "__main__":
    import sys
    sys.argv[0]
