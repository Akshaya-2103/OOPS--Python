#print n numbers using recursion. if the number is odd add 1 and print and if the number is even add 2.

def countdown(n):
    if n <= 0:
        return
    if n % 2 == 0:
        print(n+2)
    elif n % 2 != 0:
        print(n+1)
    countdown(n-1)
    if n % 2 == 0:
        print(n+2)
    elif n % 2 != 0:
        print(n+1)

countdown(5)