# 4. Theorem: For every integer k, if k > 0 then 𝑘2 +2𝑘 + 1 is composite. Write Python
# program to verify it.
# "Proof: Suppose k is any integer such that k > 0. If 𝑘2 +2𝑘 + 1 is composite, then
# 𝑘2 +2𝑘 + 1 = 𝑟𝑠 for some integers r and s such that
# 1 < 𝑟 < 𝑘2 + 2𝑘 + 1
# and
# 1 < 𝑠 < 𝑘2 + 2𝑘 + 1
# Since
# 𝑘2 + 2𝑘 + 1 = 𝑟𝑠
# and both r and s are strictly between 1 and 𝑘2 +2𝑘 + 1, then 𝑘2 +2𝑘 + 1 is not prime.
# Hence 𝑘2 +2𝑘 + 1 is composite as was to be shown."

Answer:

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

def verify_theorem(k):
    expression = k**2 + 2*k + 1
    for r in range(2, expression):
        for s in range(2, expression):
            if r * s == expression:
                print(f"Theorem is verified for k = {k}: {k}^2 + 2*{k} + 1 = {expression} = {r} * {s}")
                return True
    print(f"Theorem is not verified for k = {k}")
    return False

k_values = [1, 2, 3, 4, 5]
for k in k_values:
    verify_theorem(k)

# Output-
# Theorem is verified for k = 1: 1^2 + 2*1 + 1 = 4 = 2 * 2
# Theorem is verified for k = 2: 2^2 + 2*2 + 1 = 9 = 3 * 3
# Theorem is verified for k = 3: 3^2 + 2*3 + 1 = 16 = 2 * 8
# Theorem is verified for k = 4: 4^2 + 2*4 + 1 = 25 = 5 * 5
# Theorem is verified for k = 5: 5^2 + 2*5 + 1 = 36 = 2 * 18

