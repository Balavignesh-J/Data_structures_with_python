def  display(arr):
    for i,val in enumerate(arr):
        print(f"{i} - {val}")

def quadratic_prob(arr,val,tsize):
    i=0
    while True:
        pos = (val+i**2) % tsize
        if arr[pos]!=-1:
            i+=1
        else:
            arr[pos]=val
            break
    display(arr)

arr=[]
size=10

for i in range(size):
    arr.append(-1)

while True:
    val=int(input("Enter the value:"))
    quadratic_prob(arr,val,size)

    n=str(input("Do you wish to continue(y/n):"))
    if n.lower()=="y":
        pass
    else:
        break