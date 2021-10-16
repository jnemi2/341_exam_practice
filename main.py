

def iterative_series(n):
    result = 0
    for i in range(1, n+1):
        result += i / (i+1)
    return result


def recursive_series(n):
    if n <= 0:
        return 0
    return (n / (n+1)) + recursive_series(n-1)

print(iterative_series(1), recursive_series(1))
print(iterative_series(5), recursive_series(5))
print(iterative_series(7), recursive_series(7))
