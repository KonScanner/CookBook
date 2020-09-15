import numpy as np

M = np.array([
    [25, 0, 4, 60],
    [10, 50, 62, 5],
    [2, 30, 20, 15]
])
print(M)


sum_ = M.sum(axis=0)
print(sum_)

# % Proportion
percentage = M/sum_.reshape(1, M.shape[1])*100  # reshape is redundant
print(percentage)
