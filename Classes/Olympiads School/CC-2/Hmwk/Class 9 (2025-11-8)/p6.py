# DMOPC '17 Contest 2 P2 - Balance
from sys import stdin,stdout
def bal() -> int:
    x = stdin.readline().strip()
    res,stk = 0,[]
    for i in range(len(x)):
        cur = x[i]
        if cur == '(':
            stk.append(cur)
        elif cur == ')':
            if not stk:
                res += 1
            else:
                if cur == ')' and stk[-1] != '(':
                    res += 1
                else:
                    stk.pop()
    return res if not stk else res+len(stk)

stdout.write('YES') if bal() <= 1 else stdout.write('NO')
