# simple interest function
def simple_interest(p, r, t):
    """Calculates and returns simple interest given the principal, interest rate,
        and time in years"""
    i = p * r * t
    return i  # could also return p + i if you wanted to include principal

# compound interest function
def compound_interest(p, r, t, n):
    """Calculates and returns compound interest given the principal, interest rate,
        time in years, and number of times compounded per year"""
    a = p * (1 + r/n) ** (n * t)
    i = a - p
    return i  # could also return a if you wanted principal and interest

# when designing unit tests:
#   test more than one thing
#   test the upper and lower bounds
#   consider unexpected cases (negatives, types, etc.)

# simple unit tests
print(simple_interest(100, .10, 2))
print("Expected:", 20)

print()
print(simple_interest(5500, .07, 5))
print("Expected:", 1925)

# compound unit tests
print()
print(compound_interest(1000, .10, 5, 4))
print("Expected:", 638.62)

print()
print(compound_interest(5000, .20, 4, 2))
print("Expected:", 5717.94)






