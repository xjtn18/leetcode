
def reverse(x : int) -> int:
    x_str = str(x)
    if int(x_str.lstrip("-")) == 0 or x > 2147483647 or x < -2147483648: return 0
    rev = int( x_str.lstrip("-")[::-1].lstrip("0") )
    if rev > 2147483647 or rev < -2147483648: return 0
    return rev if x_str[0] != '-' else -rev


X = [0, -41000, -2, 100, 10, -10, 0, -0, 2147483648]

for x in X:
    print(x, ' -> ', reverse(x))
