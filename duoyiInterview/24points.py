# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @Time :2021/10/14-1:01
# @template :

def P(n, c, repeat=False, com=0, limit=0, per=[]):
    for pos in range(limit, n):
        t = per + [pos]
        if repeat or len(set(t)) == len(t):
            if len(t) == c:
                yield [pos, ]
            else:
                for result in P(n, c, repeat, com, com * pos, per + [pos, ]):
                    yield [pos, ] + result


def get_formula(l0):
    for r in res[4 - len(l0)]:
        for o in operator:
            formula = '(%s%s%s)' % (l0[r[0]], o, l0[r[1]])
            if len(l0) == 2:
                try:
                    if abs(eval(formula) - 24) < 0.1: return '%s%s%s' % (l0[r[0]], o, l0[r[1]])
                except:
                    pass
            else:
                l1 = [l0[x] for x in range(len(l0)) if not (x in r)] + [formula]
                f = get_formula(l1)
                if f != None:
                    return f
    return None


res = ([r for r in P(4, 2)], [r for r in P(3, 2)], [r for r in P(2, 2)])
operator = ('+', '-', '*', '/')

for r0 in P(11, 4, True, 1, 1):
    print(r0, get_formula([str(r) for r in r0]))
