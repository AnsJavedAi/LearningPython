# this is a single line comment
# we can use multiple single line comments 
''' this is a multi line comment to write multiple lines of comments in python
hiihaa'''
'''actually it is a docstring but we can use it as a multi line comment'''
# example 
def add(a,b):
    '''this function adds two numbers'''
    return a+b
print(add(5,10))
print(add.__doc__) # this will print the docstring of the function add
