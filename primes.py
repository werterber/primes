from testprime import testP

class Primes:
    memory = []
    
    @classmethod
    def first(cls, number):
        primes = cls.sieve(100)
        while len(primes) < number:
            primes = primes + cls.add_primes(primes)
        return primes[:number]

    def last(self, number):
        pass

    @classmethod
    def sieve(cls, number):
        numbers = [x + 1 for x in range(1, number)]
        return cls.eliminate_mutliplications(numbers)

    @staticmethod
    def filter(number, numbers):
        return filter(lambda x: x%number != 0, numbers)

    @classmethod
    def add_primes(cls, primes, count = 0):
        n = [x for x in range((primes[-1]) + 100*count, primes[-1]  + 100*(count+1))]
        for each in primes:
            n = cls.filter(each, n)
        count = 1
        while len(n) == 0:
            n = cls.add_primes(primes, count)
            count += 1

        newPrimes = cls.eliminate_mutliplications(n)
        return newPrimes

    @classmethod
    def eliminate_mutliplications(cls, numbers):
        idx = 0
        while True:
            numbers = numbers[:idx + 1] + cls.filter(numbers[idx], numbers[idx:])
            if numbers[idx] == numbers[-1]:
                break
            idx = idx + 1
        return numbers

print Primes.first(168) == testP      