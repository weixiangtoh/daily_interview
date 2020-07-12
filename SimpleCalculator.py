'''
Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. 
Assume the expression is properly formed.

Example:
Input: - ( 3 + ( 2 - 1 ) )
Output: -4
Here's the function signature:

def eval(expression):
  # Fill this in.

print eval('- (3 + ( 2 - 1 ) )')
# -4
'''
from operator import pow, truediv, mul, add, sub  

operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}

def clean_expression(expression):
  output = ""
  for i in expression:
    if i in operators or i  in ["(",")"] or i.isdigit():
      output += i
  return output

def remove_brackets(expression):
  output = ""
  for i in expression:
    if i in operators or i.isdigit():
      output += i
  return output

def calculate(stack):
  left = str()
  right = str()
  operator = str()

  if "(" in stack:
    exp = remove_brackets(stack)
  else:
    exp = stack
  # print("exp>", exp)

  if exp[0] == '-':
    left += "-"
    exp = exp[1:]

  for i in exp:
    if i.isdigit():
      left += i
    else:
      break
  for j in exp[::-1]:
    # print("j", j)
    if j.isdigit():
      right += j
    else:
      operator += j
      break
  right = int(right[::-1])
  # print("right > ",right)
  left = int(left)
  # print("left>", left)

  if operator == "+":
    return left + right
  elif operator == "-":
    return left - right
  elif operator == "*":
    return left * right
  else:
    return left / right

def eval(expression):
  # Fill this in.
  expression = clean_expression(expression)

  while "(" in expression:
    start_index = expression.rindex("(")
    end_index = expression.index(")")
    stack = expression[start_index:end_index]
    evaluated  = str(calculate(stack))
    expression = expression.replace(stack, evaluated)

  # without brackets anymore
  if ")" in expression:
    expression = remove_brackets(expression)

  while "*" in expression or "+" in expression or "/" in expression:
    expression = str(calculate(expression))
    # print("expression: ",expression)

  return expression

# does not take into account BOMUS rules for no brackets

print(eval('- (3 + ( 2 - 1 ) )'))
# -4
print(eval('- 2 + (3 + ( 2 - 1 ) )'))
# 2