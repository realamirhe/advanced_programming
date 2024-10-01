counter = 0


def fib(n, memo):
    fib.call_count += 1
    assert n >= 0, "n must be positive"
    if (memoized := memo.get(n, None)) is not None:
        return memoized
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


shared_memo = {0: 1, 1: 1}
fib.call_count = 0
fib(7, shared_memo)
print(f"called:={fib.call_count}")
fib.call_count = 0
fib(6, shared_memo)
print(f"called:={fib.call_count}")