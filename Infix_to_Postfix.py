class S:
    def __init__(self):
        self.stack=[]
        self.postfix=[]
        self.top=-1
        self.p={
            "+":1,
            "-":1,
            "*":2,
            "/":2,
            "^":3
        }

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
            return ""

    def peek(self):
        return self.stack[-1]

    def isoperand(self,ch):
        return ch.isalpha()

    def p_check(self,value):
        a=self.p[value]
        b=self.p[self.peek()]
        if a<=b:
            return True
        else:
            return False

    def result(self,n):
        for ch in n:
            if self.isoperand(ch):
                self.postfix.append(ch)
            elif ch=='(':
                self.push(ch)
            elif ch==')':
                while not self.isempty() and self.peek() != '(':
                    self.postfix.append(self.pop())
                if not self.isempty() and self.peek() == '(':
                    self.pop()
            else:
                while not self.isempty() and self.peek() != '(' and self.p_check(ch):
                    self.postfix.append(self.pop())
                self.push(ch)

        while not self.isempty():
            self.postfix.append(self.pop())

        s= "".join(self.postfix)
        print(s)
s=S()
print(f"Infix to Postfix conversion")
n=(input("Enter the Infix expression:"))
s.result(n)