import random, timeit
import poc

class Result:
    pass

def rand_hex_str(n: int) -> str:
    return ''.join(random.choice('0123456789abcdef') for _ in range(n))

random.seed(23)
STEPS = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
print('| hex digits | poc |')
for n in STEPS:
    a = int(rand_hex_str(n), base=16)
    res = Result()
    poc_t = timeit.timeit('res.out = poc.int_to_str(a)', number=4, globals=globals()) / 4
    print('| {} | {:.4f} |'.format(n, poc_t))

'''
| hex digits | poc |
| 1 | 0.0000 |
| 5 | 0.0000 |
| 10 | 0.0000 |
| 50 | 0.0000 |
| 100 | 0.0000 |
| 500 | 0.0000 |
| 1000 | 0.0000 |
| 5000 | 0.0006 |
| 10000 | 0.0017 |
| 50000 | 0.0127 |
| 100000 | 0.0290 |
| 500000 | 0.1928 |
| 1000000 | 0.4220 |
| 5000000 | 2.9880 |
'''