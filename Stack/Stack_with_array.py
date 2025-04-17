from Template import stack_template

class S:
    def __init__(self):
        self.stack=[]
        self.top=-1

    def isempty(self):
        if self.top==-1:
            return True
        else:
            return False

    def push(self,n):
        self.stack.append(n)
        self.top+=1
        print("Push success")

    def pop(self):
        if not self.isempty():
            n=self.stack.pop()
            self.top-=1
            print(f"The deleted element is {n}")
        else:
            print("stack is empty")

    def peek(self):
        if not self.isempty():
            n=self.stack[self.top]
            print(f"The Top element is {n}")
        else:
            print("stack is empty")

    def display(self):
        if not self.isempty():
            for i in range(self.top,-1,-1):
                print(f"{i+1} element is {self.stack[i]}")
        else:
            print("stack is empty")



stack_template(S,"Stack with Array")