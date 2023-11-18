# 1000206827388999999144448
# checked till 1000206827389000000027442

def is_lychrel(n1: int, limit: int = 1000) -> bool:
    for i in range(1, limit):
        n1 = str(n1)
        n2 = n1[::-1]
        n2 = int(n2)
        n1 = int(n1)
        res = n1 + n2
        res = str(res)
        if res == res[::-1] and i > 292:
            print('_' * 50)
            print('Palindromic number : {}'.format(res))
            print('_' * 50)
            print('Number of iterations : {}'.format(i))
            print('_' * 50)
            return False
        else:
            res = int(res)
            n1 = res
            continue
    else:
        return True


if __name__ == '__main__':
    for n in range(1_000_000_000_000_000_000_000_000_000_000, 2_000_000_000_000_000_000_000_000_000_000):
        if is_lychrel(n):
            print(n, 'is a failure')
        else:
            print(n, 'is a success')
            break
