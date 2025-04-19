def  display(arr):
    for i,val in enumerate(arr):
        print(f"{i} - {val}")

def linear_prob(arr,val,tsize):
    pos = val % tsize
    while arr[pos]!=-1:
        pos=(pos+1)%tsize
    arr[pos]=val
    display(arr)

arr=[]
size=10

for i in range(size):
    arr.append(-1)

while True:
    val=int(input("Enter the value:"))
    linear_prob(arr,val,size)

    n=str(input("Do you wish to continue(y/n):"))
    if n=="y":
        pass
    else:
        break