import random, timeit
import poc

class Result:
    pass

def rand_dec_str(n: int) -> str:
    return ''.join(random.choice('0123456789') for _ in range(n))

STEPS = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
print('| dec digits | poc | std | result |')
for n in STEPS:
    a = rand_dec_str(n)
    res = Result()
    poc_t = timeit.timeit('res.out = poc.str_to_int(a)', number=1, globals=globals())
    std_t = timeit.timeit('res.ans = int(a)', number=1, globals=globals())
    print('| {} | {:.4f} | {:.4f} | {} |'.format(n, poc_t, std_t, 'Correct' if res.out == res.ans else 'Wrong'))

'''
| dec digits | poc | std | result |
| 1 | 0.0000 | 0.0000 | Correct |
| 5 | 0.0000 | 0.0000 | Correct |
| 10 | 0.0000 | 0.0000 | Correct |
| 50 | 0.0000 | 0.0000 | Correct |
| 100 | 0.0000 | 0.0000 | Correct |
| 500 | 0.0000 | 0.0000 | Correct |
| 1000 | 0.0000 | 0.0000 | Correct |
| 5000 | 0.0002 | 0.0001 | Correct |
| 10000 | 0.0004 | 0.0004 | Correct |
| 50000 | 0.0051 | 0.0105 | Correct |
| 100000 | 0.0142 | 0.0413 | Correct |
| 500000 | 0.1898 | 1.0357 | Correct |
| 1000000 | 0.5624 | 4.1387 | Correct |
'''