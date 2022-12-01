#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    from sys import argv, exit

    if len(argv) - 1 != 3:
        if len(argv) - 1 != 3:
            exit(1)

    elif argv[2] == "+":
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     cal.add(int(argv[1]), int(argv[3]))))
    elif argv[2] == "-":
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     cal.sub(int(argv[1]), int(argv[3]))))
    elif argv[2] == "*":
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     cal.mul(int(argv[1]), int(argv[3]))))
    elif argv[2] == "/":
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     cal.div(int(argv[1]), int(argv[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
