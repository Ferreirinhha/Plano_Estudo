# Fatorial


def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)
    

print(fatorial(3))

#Fibonati


def fibonati(num):
    if num == 1 or num == 2:
        return num - 1
    else:
        return fibonati(num - 1) + fibonati(num - 2)


print(fibonati(20))