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

    def pop(self):
        if not self.isempty():
            n=self.stack.pop()
            self.top-=1
            return n
        else:
            return 0

    def peek(self):
        return self.stack[-1]

    def isnumber(self,ch):
        return ch.isnumeric()

    def result(self,n):
        for ch in n:
            if self.isnumber(ch):
                self.push(int(ch))
            else:
                a=self.pop() 
                b=self.pop() 
                self.push(eval(f'{b} {ch} {a}'))
                
         
                    

        print(self.pop())
   
s=S()
print("Postfix Evaluation")
n=(input("Enter the Postfix expression:"))
arr=n.strip().split()
s.result(arr)
