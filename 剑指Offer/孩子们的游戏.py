

# f(n) = (f(n-1) + m) % n
# f(1) = 0
def LastRemaining_Solution(n, m):
    if n < 1 or m < 1:
        return -1
    if n == 1:
        return 0
    value = 0
    for index in range(2, n+1):
       value = (value + m) % index
    return value

