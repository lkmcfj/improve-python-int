import random, timeit
import poc

class Result:
    pass

def rand_hex_str(n: int) -> str:
    return ''.join(random.choice('0123456789abcdef') for _ in range(n))

STEPS = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
print('| hex digits | poc | std | result |')
for n in STEPS:
    a = int(rand_hex_str(n), base=16)
    res = Result()
    poc_t = timeit.timeit('res.out = poc.int_to_str(a)', number=1, globals=globals())
    std_t = timeit.timeit('res.ans = str(a)', number=1, globals=globals())
    print('| {} | {:.4f} | {:.4f} | {} |'.format(n, poc_t, std_t, 'Correct' if res.out == res.ans else 'Wrong'))

'''
| hex digits | poc | std | result |
| 1 | 0.0000 | 0.0000 | Correct |
| 5 | 0.0000 | 0.0000 | Correct |
| 10 | 0.0000 | 0.0000 | Correct |
| 50 | 0.0000 | 0.0000 | Correct |
| 100 | 0.0000 | 0.0000 | Correct |
| 500 | 0.0000 | 0.0000 | Correct |
| 1000 | 0.0001 | 0.0000 | Correct |
| 5000 | 0.0007 | 0.0005 | Correct |
| 10000 | 0.0018 | 0.0021 | Correct |
| 50000 | 0.0141 | 0.0517 | Correct |
| 100000 | 0.0300 | 0.2042 | Correct |
| 500000 | 0.2029 | 5.0972 | Correct |
| 1000000 | 0.4310 | 20.3772 | Correct |
'''