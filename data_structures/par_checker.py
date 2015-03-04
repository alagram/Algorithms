from stack import *
def parChecker(symbolString):
    stack = Stack()
    for i in symbolString:
        if i == "(":
            stack.push(i)
        else:
            if not stack.isEmpty():
                stack.pop()
    if stack.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))
