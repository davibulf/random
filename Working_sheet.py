#  from swampy.TurtleWorld import *
import math


#  world = TurtleWorld()
#  bob = Turtle()
#  bob.delay = 0.01
#  print(bob)


def lyrics():
    w = "And they don't stop coming"
    print(w)


def repeat_lyrics():
    lyrics()
    lyrics()


def boy(n):
    print(n, end=" ")
    print(" good boy")


def girl(m):
    print(m, end=" ")
    print(" good girl")


# x !=y    x is not equal to y
# x>y      x is greater than y
# x<y      x is less than y
# x>=y     x is greater than or equal to y
# x>=y     x is less than or equal to y


def do_n(f, n):
    if n == 0:
        return
    print(f)
    do_n(f, n - 1)


def recurse():
    recurse()


def nice_detector():
    prompt = "What is nice?\n"
    p = input(prompt)
    if p == "boobies":
        print("\033[1;32;40m that's nice\n")
    elif p != "boobies":
        print("\033[1;31;40m Not nice\n")
        nice_detector()


#  def move(t):
#    pu(t)
#    fd(t, 200)
#    rt(t, 90)
#    fd(t, 300)
#    rt(t, 270)
#    pd(t)


#  def koch(t, n):
#    """Draws a koch curve with length n."""
#    if n < 3:
#        fd(t, n)
#       return
#   m = n / 3.0
#    koch(t, m)
#    lt(t, 60)
#    koch(t, m)
#    rt(t, 120)
#    koch(t, m)
#    lt(t, 60)
#    koch(t, m)


#  wait_for_user()

def area(radius):
    return math.pi * radius ** 2


def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x
    if x == 0:
        return x


def absolute_value_2(x):
    return abs(x)


def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    squared = dx ** 2 + dy ** 2
    result = math.sqrt(squared)
    return result


def hypotenuse(x, y):
    pythagoras = math.sqrt(x ** 2 + y ** 2)
    return pythagoras


def circle_area(xc, yc, xp, yp):
    #  radius = distance(xc, yc, xp, yp)
    #  result = area(radius)
    return area(distance(xc, yc, xp, yp))


def is_divisible(x, y):
    return x % y == 0


def is_between(x, y, z):
    return not (x <= y <= z) == 0


def factorial(n):
    if not isinstance(n, int):
        print("Factorial is only defined for integers")
        return None
    elif n < 0:
        print("Factorial is not defined for negative integers")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print("Blastoff !")


def print_n(s, n):
    if n <= 0:
        return
    while n > 0:
        print(s)
        n = n - 1


#  print_n("Hello", 5)


def square_root(a):
    epsilon = 0.00001
    x = a - 1
    while x > epsilon:
        y = (x + a/x) / 2
        if abs(a) < epsilon:
            pass
        elif x == y:
            return x
        else:
            x = y


#  print(type(square_root(64)))


def check_square_root(a):
    for i in range(a - 1):
        b = math.sqrt(a)
        k = abs(square_root(a))
        z = abs(b - k)
        print(a, end=" ")
        print(b, end=" ")
        print(k, end=" ")
        print(z, end=" ")
        print(end="\n")
        a = a - 1

    print("1", end=" ")
    print("1", end=" ")
    #  print("1", end=" ")
    #  print("0", end=" ")
    print(end="\n")


#  check_square_root(420)


fruit = "banana"
# letter = fruit[0]
last = fruit[len(fruit)-1]
last_2 = fruit[-1]
#  print(len(fruit))
#  print(letter)
#  print(last)
#  print(last_2)
#
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index + 1

# for char in fruit:
#     print(char)

prefixes = "JKLMOPQ"
suffix = "ack"

# for letter in prefixes:
#     print(letter + suffix)

# word = "banana"
# new_word = word.upper()
# index = word.find("na", 3)
# print(new_word)
# print(index)
#
# name = "bob"
# name.find("b", 1, 2)
# print(name.find)
# #
# word = "banana"
# letter_a_count = word.count("a")
# print(letter_a_count)
# strip = word.strip("b, a")
# print(strip)
# replace = word.replace("n", "l")
# print(replace)
#
# print("a" in "banana")
# print("seed" in "banana")


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter, end=" ")


#   in_both("apples", "oranges")

