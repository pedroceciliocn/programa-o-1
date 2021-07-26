def palindromo(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False
    return palindromo(s[1:-1])

print(palindromo('abba'))
print(palindromo(404)) # ih