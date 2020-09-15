import numpy as np

A = np.random.randn(5)
print(A)

print(A.shape)


print(A.T)

print(np.dot(A, A.T))  # not what you'd expect

# Instead, learn to work this way, making it a column or row vector:
A = np.random.randn(5, 1)  # col vec
assert (A.shape == (5, 1))
assert (A.T.shape == (1, 5))  # row vec

print(A, A.T)

print(np.dot(A, A.T))
