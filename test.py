import requests
import config
import timeit
import random
import matplotlib.pyplot as plt

random.seed(1)

numbers = [random.randint(50, 150) for i in range(100)]


def func1():
    for i in range(2, 100):
        if numbers[i - 2] > numbers[i - 1] > numbers[i]:
            pass


def func2():
    for i in range(2, 100):
        if numbers[i - 1] > numbers[i]:
            if numbers[i - 2] > numbers[i - 1]:
                pass


number = 2000
repeat = 200

line1 = [
    round(i, 4)
    for i in timeit.repeat(
        "func1()", "from __main__ import func1", number=number, repeat=repeat
    )
]

line2 = [
    round(i, 4)
    for i in timeit.repeat(
        "func2()", "from __main__ import func2", number=number, repeat=repeat
    )
]

    


plt.plot(line1, label="c>b>a")
plt.plot(line2, label="if a<b if b<c")
plt.legend()
plt.show()
