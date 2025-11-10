# more memory saving and faster
N = int(input())

def main(n):
    days = []
    for i in range(n):
        days.append(True) if input() == 'S' else days.append(False)
    if n == 1:
        print(1)
        return
    elif all(days):
        print(n)
        return



    left,subm,violation = 0,0,False
    for i in range(n):
        cd = days[i]
        try:
            if cd:
                left = i
            elif not cd and days[i+1] == True and days[i-1] == True and not violation:
                violation = True
            else:
                subm = max(subm,i-left)
        except IndexError:
            subm = max(subm,i-left)

    print(subm)
main(N)

# inefficient and also broken
"""
N = int(input())
# days = []
chunks = []
curChunk = [0,0,0]
last = False
for i in range(N):
    if input() == "S":
        # days.append(True)
        if not last:
            last = True
            curChunk[0] = i
        if last:
            curChunk[2] += 1
            if i == N-1:
                curChunk[1] = i
                chunks.append(curChunk)
    else:
        # days.append(False)
        if last:
            last = False
            curChunk[1] = i-1
            chunks.append(curChunk)
            curChunk = [0,0,0]


def main() -> int:
    if not chunks:
        return curChunk[2]
    if len(chunks) == 1:
        return chunks[0][2]

    semimax = 0
    for i in range(1,len(chunks)):
        try:
            if chunks[i][0] == chunks[i-1][1]+2:
                semimax = max(semimax,chunks[i][2]+chunks[i-1][2]+1)
            if chunks[i][0] == chunks[i+1][1]-2:
                semimax = max(semimax,chunks[i][2]+chunks[i+1][2]+1)
        except IndexError:
            break
    return semimax

    

print(main())
"""




