from math import ceil # ceil always rounds up to whole number


def is_prime(num):
    top = int(ceil(num ** 0.5)) # a number takes sqroot and rounds to whole number gives that integer
    for x in range(3, top + 1, 2): # range of (3  to top + 1, by 2) add one beacuse takes out perfect squares
        if num % x == 0: # remainder is 0 retrun false
            return False
    return True

def primes(max=10):
    yield 2 # generator that resumes where it left off loops
    found = 1 # defines initial value of found
    current = 3 # defines initial value current
    while found < max:
        if is_prime(current):
            yield current # take the number similar to "return" allows to loop not end
            found += 1 # found + 1
        current += 2 # current + 2 skips over the even numbers

for prime in primes(10001): # find 10001 primes
    print prime # print them

# figure out way just to print the answer not the whole 10001 list
