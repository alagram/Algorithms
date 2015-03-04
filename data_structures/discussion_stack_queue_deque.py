"""
# Binanty conversion with Divide by 2
from stack import *

def divide_by_2(num):
    stack = Stack()

    while num > 0:
        rem = num % 2
        stack.push(rem)
        num = num // 2

    bin_num = ""

    print(stack.items)

    while not stack.isEmpty():
        bin_num += str(stack.pop())

    return bin_num


print(divide_by_2(96))
# """
# from stack import *

# def infix_to_postfix(token_input):
#     stack = Stack()
#     postfix_list = []

#     order_mag = {}
#     order_mag["/"] = 4
#     order_mag["*"] = 4
#     order_mag["+"] = 3
#     order_mag["-"] = 2
#     order_mag["("] = 1

#     for token in token_input:
#         if token in "ABCDEFGHIJKLMNOPQRST" or token in "0123456789":
#             postfix_list.append(token)
#             print(stack.items)
#         elif token == "(":
#             stack.push(token)
#             print(stack.items)
#         elif token == ")":
#             top = stack.pop()
#             while top != "(" and not stack.isEmpty():
#                 postfix_list.append(top)
#                 top = stack.pop()
#             print(stack.items)
#         else:
#             while not stack.isEmpty() and order_mag[stack.peek()] >= order_mag[token]:
#                 postfix_list.append(stack.pop())
#             stack.push(token)
#             print(stack.items)

#     while not stack.isEmpty():
#         postfix_list.append(stack.pop())

#     return " ".join(postfix_list)

# print(infix_to_postfix("(A+B)*(C+D)*(E+F)"))


from stack import *
def postfix_eval(input_str):
    stack = Stack()
    token_list = input_str.split()
    for token in token_list:
        if token in "0123456789":
            stack.push(token)
        else:
            second_opr = int(stack.pop())
            first_opr = int(stack.pop())
            result = evaluate(token, first_opr, second_opr)
            stack.push(result)

    return stack.pop()

def evaluate(operator, opr_1, opr_2):
    if operator == "/":
        return opr_1 / opr_2
    elif operator == "*":
        return opr_1 * opr_2
    elif operator == "+":
        return opr_1 + opr_2
    else:
        return opr_1 - opr_2

print(postfix_eval("1 2 3 4 5 * + * +"))
