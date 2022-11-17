a = int(input("What would you like your first number to be?"))
b = int(input("What would you like your second number to be?"))

c = a + b
# addition_function is adding two inputs
def addition_function(x, y):
    z = x + y
    return z

# d =  subtraction result
def subtraction_function(x, y):
    z = x - y
    return z

d = a - b
# e = multiplication of a and b
def multiplication_function(x, y):
    z = x * y
    return z

# F is division of a over b
f = a / b
def division_function(x, y):
    z = x / y
    return z

def ratio(x, y, report_percent=True):
    new_ratio = x / (x + y)
    percent_ratio = (x / (x+y)) * 100
    if report_percent = True:
        return percent_ratio
    elif report_percent = False:
        return new_ratio


