def counting_block_1(N):
    if N<0 :
        return 0
    count_block = [1,1,1,2]
    if N<len(count_block):
        return count_block[N]
    else :
        for i in range(4,N+1):
            value = 0
            for j in range(0,i-3):
                value += count_block[j]
            value = value + count_block[i-1]+1
            count_block.append(value)
    return count_block[N]

def counting_block_2(N,m):

    if N<0 :
        return 0
    count_block = [1]*m
    count_block.append(2)
    if N<len(count_block):
        return count_block[N]
    else :
        for i in range(m+1,N+1):
            value = 0
            for j in range(0,i-m):
                value += count_block[j]
            value = value + count_block[i-1]+1
            count_block.append(value)
    return count_block[N]

def over_million_block(m):
    over_million = False
    N=m
    while not(over_million):
        N += 1
        over_million = counting_block_2(N,m)>1000000
    print(N)
    return N

print(over_million_block(50))
