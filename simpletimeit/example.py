import stimeit

time_args = (100, 500)


@stimeit.time_this(func_input=time_args, group='primes')
def check_all(n):
    result = []
    for i in range(2, n + 1):
        if not any((i % x) == 0 for x in range(2, i)):
            result.append(i)
    return result

@stimeit.time_this(func_input=time_args, group='primes', ref=check_all)
def sieve(n):
    flags = [True for _ in range(n + 1)]
    flags[0] = flags[1] = False
    for i in range(len(flags)):
        if flags[i]:
            for j in range(i + 1, len(flags)):
                if flags[j] and j % i == 0:
                    flags[j] = False

    return [i for i, f in enumerate(flags) if f]

@stimeit.time_this(func_input=time_args, group='primes', ref=check_all)
def memoized(n, _primes={}):
    result = []
    for i in range(2, n + 1):
        if i not in _primes:
            _primes[i] = not any(i % x == 0 for x in range(2, i))
        if _primes[i]:
            result.append(i)

    return result

@stimeit.time_this(func_input=('range(100)', 'range(1000000)'), group='flatten')
def with_list(iterator):
    return list(iterator)


@stimeit.time_this(func_input=('range(100)', 'range(1000000)'), group='flatten')
def with_tuple(iterator):
    return tuple(iterator)

if __name__ == '__main__':
    stimeit.run()


