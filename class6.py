
number = input("輸入a:")
a = int(number)
number = input("輸入b:")
b = int(number)

print("=== 算術運算子 ===")

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

print("\n=== 比較運算子 ===")
print(f"{a} == {b} → {a == b}")
print(f"{a} != {b} → {a != b}")
print(f"{a} > {b} → {a > b}")
print(f"{a} < {b} → {a < b}")
print(f"{a} >= {b} → {a >= b}")
print(f"{a} <= {b} → {a <= b}")

print("\n=== 邏輯運算子 ===")
x = True
y = False
print(f"{x} and {y} → {x and y}")
print(f"{x} or {y} → {x or y}")
print(f"not {x} → {not x}")

print("\n=== 賦值運算子 ===")
c = 5
print(f"初始 c = {c}")
c += 2
print(f"c += 2 → {c}")
c -= 1
print(f"c -= 1 → {c}")
c *= 3
print(f"c *= 3 → {c}")
c //= 2
print(f"c //= 2 → {c}")
c %= 4
print(f"c %= 4 → {c}")
