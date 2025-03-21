def bubble(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if swapped:
            continue
        else:
            break

def selection(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min=j
        if min!=i:
            arr[min],arr[i]=arr[i],arr[min]

def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        cur=arr[i]
        j=i-1
        while j>=0 and arr[j]>cur:

            arr[j+1]=arr[j]
            j-=1

        arr[j+1]=cur

arr=[5,1,4,2,3]
insertion(arr)
print(arr)
