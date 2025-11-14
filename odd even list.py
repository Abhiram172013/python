# Ask user for range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# List to store squared values
squares = []

for num in range(start, end + 1):
    squares.append(num * num)

# Separate even and odd squares
even_squares = []
odd_squares = []

for sq in squares:
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

# Display results
print("All square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)
