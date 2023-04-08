def base(n):
    if n == 0:
        return '0'
    num_list = []
    while n:
        n, r = divmod(n, 3)
        num_list.append(str(r))
    return ''.join(reversed(num_list))
print(base())
