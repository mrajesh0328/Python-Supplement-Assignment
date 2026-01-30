# Problem 79: Calculate compound interest
# Find and fix the error

def compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    return amount - principal

p = 1000
r = 5
t = 1
n = 4
print(f"Compound Interest: {compound_interest(p, r, t, n)}")
