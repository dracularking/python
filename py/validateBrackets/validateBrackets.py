class stack: 
  def __init__(self): 
    self.items = []      
  def push(self,item):   
    self.items.insert(0,item) 
  def pop(self): 
    return self.items.pop(0) 
  def __call__(self): 
    return self.items 


def balanced(expression):
    x = stack() 
    for char in expression: 
      if char == '(': 
        x.push(char) 
      if char == ')': 
        if '(' in x(): 
          x.pop() 
        else: 
          return False 
    if not x(): 
      return True 
    return False

print(balanced(input()))
