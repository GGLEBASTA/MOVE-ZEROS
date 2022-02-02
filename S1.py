def move_zeros(s):
    for i in s:
        if(i == 0):
            s.append(s.pop(s.index(i)))
            continue
        else:
            continue
    return s

m = move_zeros([1, 0, 1, 2, 0, 1, 3])
print(m)
