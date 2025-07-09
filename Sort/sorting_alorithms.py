from template import sorting_template

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

def merge(arr):
    if len(arr)>1:
        m=len(arr)//2
        left=arr[:m]
        right=arr[m:]

        merge(left)
        merge(right)

        lp=0
        rp=0
        ap=0

        while lp<len(left) and rp<len(right):
            if left[lp]<right[rp]:
                arr[ap]=left[lp]
                lp+=1
            else:
                arr[ap]=right[rp]
                rp+=1
            ap+=1

        while lp<len(left):
            arr[ap]=left[lp]
            lp+=1
            ap+=1

        while rp<len(right):
            arr[ap]=right[rp]
            rp+=1
            ap+=1

def quick(arr,left,right):
    if left < right:
        pos = pivotpos(arr,left,right)
        quick(arr,left,pos-1)
        quick(arr,pos+1,right)

def pivotpos(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]

    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]

    return i

#arr=[5,1,4,2,3,6,8,7,9]
sorting_template()