counter = 0


def fib(n, memo):
    global counter
    assert n >= 0, "n must be positive"
    if (memoized := memo.get(n, None)) is not None:
        return memoized
    counter += 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


shared_memo = {0: 1, 1: 1}
fib(7, shared_memo)
print(counter)
counter = 0
fib(6, shared_memo)
print(counter)
