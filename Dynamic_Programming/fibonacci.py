def bottom_up(n):
    arr=[0]*n
    arr[0]=1
    arr[1]=1
    for i in range(2,n):
        arr[i]=arr[i-1]+arr[i-2]

    return arr[n-1]

def top_down(pos,memory={}):
    if pos in memory:
        return memory[pos]
    if pos<=2:
        return 1
    memory[pos]=top_down(pos-1,memory)+top_down(pos-2,memory)

    return memory[pos]

n=10

print(f"Bottom up approach {n} is {bottom_up(n)}")
print(f"Top down approach {n} is {top_down(n)}")