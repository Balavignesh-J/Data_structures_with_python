def  display(arr):
    for i,val in enumerate(arr):
        print(f"{i} - {val}")

def double_prob(arr,val,tsize):
    while True:
        pos = 7 - (val%tsize)
        if arr[pos]==-1:
            arr[pos]=val
            break
    display(arr)

arr=[]
size=10

for i in range(size):
    arr.append(-1)

while True:
    val=int(input("Enter the value:"))
    double_prob(arr,val,size)

    n=str(input("Do you wish to continue(y/n):"))
    if n.lower()=="y":
        pass
    else:
        break