# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = int(input('Введите целое число больше 1: '))
startA = a
n = 3
f = 1.618
while a > 2:
    a = a / f
    n += 1
fib = round((f**n - (1-f)**n) / 5 ** 0.5)
if fib == startA:
    print(n + 1)
else:
    print(-1)

# a = int(input('Введите целое число больше 1: '))
# if a == 0:
#     print(0)
# else:
#     fib_prev, fib_next = 0, 1
#     n = 18
#     while fib_next <= a:
#         if fib_next == a:
#             print(n + 1)
#             break
#         fib_prev, fib_next = fib_next, fib_prev + fib_next
#         n += 1
#     else:
#         print(-1)
