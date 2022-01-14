# python3
import time

def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    F = [0,1]
    f_60 = n % 60

    if f_60 < 2:
        return f_60
    for i in range(2, f_60 + 1):
        current = F[1] + F[0]
        F[0] = F[1]
        F[1] = current
    return F[1] % 10

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))