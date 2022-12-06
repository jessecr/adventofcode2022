def solve(text, n):
    for i in range(n - 1, len(text)):
        if len(set(text[i - n:i])) == n:
            return i


text = open('input').read()
print(solve(text, 4))
print(solve(text, 14))
