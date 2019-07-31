# def add_five(num): 
#     return num + 5 
    

# def test_add_five(): 
#     assert add_five(3) == 8


def factorial(n): 
    if n == 1: 
        return 1 
    else: 
        return n * factorial(n-1) 


def test_factorial(): 
    assert factorial(5) == 120

