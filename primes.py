"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    for number in range (0, number_of_primes+1):
        prime = True
        if number > 1:
            prime = False
            for i in range (2, number):
                if (number % i) == 0:
                    prime = False
            if prime:
                list.append(number)
    print(list)
    return list
