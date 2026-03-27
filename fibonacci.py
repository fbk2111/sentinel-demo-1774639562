fibonacci_sequence = []
a, b = 0, 1
for _ in range(10):
    fibonacci_sequence.append(a)
    a, b = b, a + b
print(fibonacci_sequence)