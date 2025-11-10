# DMOPC '21 Contest 7 P2 - Knitting Scarves
N,Q = map(int,input().split())
ops = [list(map(int, input().split())) for i in range(Q)]
# N,Q = 6,3
# ops = [
#     [4,5,1],
#     [5,6,0],
#     [2,2,3]
# ]
scarf = [i+1 for i in range(N)]


# second edition, let's try and make this O(1) space



# first edition, most basic and intuitive solution, **MEMORY EXCEEDED**
"""
for i in range(Q):
    if ops[i][2] == 0:
        if ops[i][0] == ops[i][1]:
            tmp = scarf[scarf.index(ops[i][0])]
            scarf.remove(tmp)
            scarf.insert(0,tmp)
        else:
            li,ri = scarf.index(ops[i][0]),scarf.index(ops[i][1])+1
            # s,l,r = scarf[li:ri],scarf[:li],scarf[ri:]
            # scarf = s + l + r
            scarf = scarf[li:ri] + scarf[:li] + scarf[ri:]
    else:
        if ops[i][0] == ops[i][1]:
            tmp = scarf[scarf.index(ops[i][0])]
            scarf.insert(scarf.index(ops[i][2])+1,tmp)
            scarf.remove(tmp)
        else:
            li,ri,ki = scarf.index(ops[i][0]),scarf.index(ops[i][1])+1,scarf.index(ops[i][2]) + 1
            # ll,s,lr,r = scarf[:li][:ki],scarf[li:ri],scarf[:li][ki:],scarf[ri:]
            # scarf = ll + s + lr + r
            scarf = scarf[:li][:ki] + scarf[li:ri] + scarf[:li][ki:] + scarf[ri:]
"""

print(scarf)


