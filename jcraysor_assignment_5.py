# TEST CASE 2: Prime Number Checker

print("=== Challenge 2: Prime Number Checker ===")
num = int(input("Enter a number: "))

if num > 1: # No negative values are needed for this test case
    print(f"Testing divisors from 2 to {num - 1}...")
    for i in range(2, num - 1):
        if num % i == 0: # If the remainder is equal to 0, it's not prime.
            print(f"{num} is not prime (divisible by {i})")
            break
    else:
        print(f"{num} is prime!")
else:
    print(f"{num} is not prime")
print()

# TEST CASE 3: Multiplication Table
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication table:")
print("", end="")

# header numbers
for header in range(1, 11):
    print(f"{header:4}", end="")
print()

# Loops presenting the rows, columns, and products for the table
for row in range(1, 11): # 1 is inclusive in the range, 11 is excluded (so 10 is technically the max value in the output)
    print(f"{row:2}", end="")
    for col in range(1, 11):
        table_value = row * col # Products come from multiplying rows and columns
        print(f"{table_value:4}", end="")
    print()

