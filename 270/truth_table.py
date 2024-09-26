
def func_3(w, x, y, z):
    p1 = not (w and (not z))
    p2 = not (w and (not x))
    p3 = not (y and (not x))
    p4 = not (y and (not z))
    return not (p1 and p2 and p3 and p4)

def func_4(w, x, y, z):
    p1 = not (w or y)
    p2 = not ((not x) or (not z))
    return not (p1 or p2)



def func_2(w, x, y, z):
    return (not ((not w) and (not y))) and (not (x and z))

def func_1(w, x, y, z):
    return (w and (not z)) or (w and (not x)) or (y and (not z)) or (y and (not x))

def main():
    print('w x y z | f1 f2  f4')
    print('--------|-----')
    for w in [False, True]:
        for x in [False, True]:
            for y in [False, True]:
                for z in [False, True]:
                    print(f'{int(w)} {int(x)} {int(y)} {int(z)} | {int(func_1(w, x, y, z))}  {int(func_2(w, x, y, z))}  {int(func_4(w, x, y, z))}')


if __name__ == '__main__':
    main()
