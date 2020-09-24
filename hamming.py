

def is_even(n):
    assert type(n) == int
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

# message length 11
message = [0,NA,NA,0,NA,0,0,0,NA,0,0,0,0,0,0]

def get_parities(message):
    # LHS
    pass