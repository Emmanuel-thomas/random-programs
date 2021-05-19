for i in range(10):
    for j in range(9, 0, -1):
        print(" " * j, end='')
        for i in range(10):
            print("*" * i, end='')
