# 3. Assume that m and n are particular integers. Write Python program to verify it.
# a. Is 6m + 8n even?
# b. Is 10mn + 7 odd?
# c. If m > n > 0, is 𝑚2 ― 𝑛2 composite?

# Answer:

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

def verify_conditions(m, n):
    condition_1 = is_even(6*m + 8*n)
    condition_2 = is_odd(10*m*n + 7)
    condition_3 = is_composite(m**2 - n**2)
    
    print(f"Is 6m + 8n even? {condition_1}")
    print(f"Is 10mn + 7 odd? {condition_2}")
    print(f"If m > n > 0, is m^2 - n^2 composite? {condition_3}")

m = 3
n = 2
verify_conditions(m, n)

# Output -
# Is 6m + 8n even? True
# Is 10mn + 7 odd? True
# If m > n > 0, is m^2 - n^2 composite? False
