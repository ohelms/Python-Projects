import ctypes


def main():



    x = 0 
    y = 0
    problem = input("Operation: ").split()
    if problem == ["q"]:
        return None
    function = problem[0]
    x = int(problem[1])
    y = 0
    if len(problem) > 2:
        y = int(problem[2])
    
    answer = functions_select(function, x, y)

    print("Answer: {0}".format(answer))
    return main()



def add(x, y):
    if y == 0:
        return x
    carry = x & y
    cx = ctypes.c_int64(x ^ y)
    cy = ctypes.c_int64(carry << 1)
    return add(cx.value, cy.value)



def neg(x):
    return add(~x, 1)



def sub(x, y):
    return add(x, neg(y)) 



def mul(x, y):
    if x == 0:
        return 0
    elif x == 1:
        return y
    elif x < 0 and y < 0:
        return add(abs(y), mul(add(abs(x), neg(1)), abs(y)))
    elif x < 0 or y < 0:
        return neg(add(abs(y), mul(add(abs(x), neg(1)), abs(y))))
    else:
        return add(y, mul(add(x, neg(1)), y))



def exp(x, y):
    if x == 0:
        return 0
    elif x == 1:
        return x
    elif y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return mul(x, exp(x, add(y, neg(1))))



def div(x, y):
    floor = 2
    if y == 0:
        return None
    elif abs(x) < y:
         return 0
    elif x < 0 and y < 0:
         return (add (1, div(add(abs(x), neg(abs(y))), abs(y))))
    elif (x < 0 or y < 0) and mod(x,y)==0:
        return neg(add(1, div(add(abs(x), neg(abs(y))), abs(y))))    
    elif x < 0 or y < 0:
         return neg(add(floor, div(add(abs(x), neg(abs(y))), abs(y))))
    else:
         return (add(1, div(add(x, neg(y)), y)))



def mod(x,y):
    if abs(x) < abs(y) and ((y > 0 and x >= 0) or (y < 0 and x <= 0)):
        return x
    elif abs(x) < abs(y):
        return add(x, y)
    elif abs(x) >= abs(y) and ((y > 0 and x >= 0) or (y < 0 and x <= 0)):
        return mod(add(x, neg(y)), y)
    elif abs(x) >= abs(y) and ((y > 0 and x < 0) or (y < 0 and x > 0)):
        return mod(add(x, y), y)
    else:
        return None



def fac(x, result):
    if x == neg(1):
        return None
    if x == 0:
        return result
    return fac(sub(x, 1), mul(x, result))



def fib(x, result, fib_num):
    if x == neg(1):
        return None
    if x == 0:
        return result[-2:-1][0]
    result.append(fib_num)
    return fib(sub(x, 1), result, add(result[-2], result[-1]))



def functions_select(function, x, y):
    if function == "add":
        return add(x, y)
    elif function == "neg":
        return neg(x)
    elif function == "sub":
        return sub(x, y)
    elif function == "mul":
        return mul(x, y)
    elif function == "exp":
        return exp(x, y)
    elif function == "div":
        return div(x, y)
    elif function == "mod":
        return mod(x, y)
    elif function == "fac":
        return fac(x, 1)
    elif function == "fib":
        return fib(x, [0, 1], 1) 



if __name__ == "__main__":
    main()