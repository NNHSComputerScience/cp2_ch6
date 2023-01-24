# Notes on Unit Testing

# UNIT TEST - test if a function works on its own.
# INTEGRATION TEST - test if a function works with other functions (possibly in a main section of code)

# simple interest function
#    simple interest formula is i = p * r * t
#    i = interest
#    p = principal
#    r = rate of return
#    t = time

def simple_interest(p, r, t):
	"""Calculates and returns simple interest given a principal dollars, rate as a decimal, and time in years"""
	i = p * r * t
	return i

# compound interest function
def compound_interest(p, r, t, n):
    """Calculates and returns compound interest given the principal, interest rate,
        time in years, and number of times compounded per year"""
    a = p * (1 + r/n) ** (n * t)
    i = a - p
    return i  # could also return a if you wanted principal and interest

# when designing unit tests:
#		- test more than one thing
#		- test the upper and lower bounds
#		- consider unexpected cases (negatives, types, etc.)
# NOTE: you may have to deal with the imprecision of floating point values when testing numbers, in which case you want to test if teh expected value is 'close enough'


# simple unit tests
print("Actual: ", simple_interest(100, .10, 2))
print("Expected: ", 20.0)

print()
result = simple_interest(5500, .07, 5)
print("Actual:", result)
print("Expected:", 1925.0)
print("Pass test?", result - 1925.0 < 0.001)

# compound interest unit tests
print()
result = compound_interest(1000, .10, 5, 4)
print("Actual:", result)
print("Expected:", 638.62)
print("Pass test?", result - 638.62 < 0.005)

print()
result = compound_interest(5000, .20, 4, 2)
print("Actual:", result)
print("Expected:", 5717.94)
print("Pass test?", result - 5717.94 < 0.005)
