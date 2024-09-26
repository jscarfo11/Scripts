
def func_1(a, b, c):
    return a or (b and c)

def func_2(a, b, c):
    return (a or b) and c



def main():
    print('w x y | f1 f2  f4')
    print('--------|-----')
    for w in [False, True]:
        for x in [False, True]:
            for y in [False, True]:
                for z in [False, True]:
                    print(f'{int(w)} {int(x)} {int(y)} | {int(func_1(w, x, y))}  {int(func_2(w, x, y))}')


if __name__ == '__main__':
    main()
