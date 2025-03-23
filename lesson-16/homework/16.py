import numpy as np

dtype = [('position', [('x', float), ('y', float)]), 
         ('color', [('r', int), ('g', int), ('b', int)])]

array = np.array([((1.0, 2.0), (255, 0, 0)), 
                  ((3.0, 4.0), (0, 255, 0)), 
                  ((5.0, 6.0), (0, 0, 255))], dtype=dtype)

print(array)


from scipy.spatial import distance

coords = np.random.rand(100, 2)
dist_matrix = distance.cdist(coords, coords, metric='euclidean')

print(dist_matrix)


arr = np.random.rand(5).astype(np.float32)
arr = arr.view(np.int32)
print(arr)



import pandas as pd

data = pd.read_csv("data.txt", header=None)
print(data.fillna(0))  # Replace NaN with 0



Z = np.array([10, 20, 30, 40])
for index, value in np.ndenumerate(Z):
    print(index, value)



x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
gaussian = np.exp(- (x**2 + y**2))
print(gaussian)


p = 5
arr = np.zeros((10, 10))
indices = np.random.choice(arr.size, p, replace=False)
arr.flat[indices] = 1
print(arr)



Z = np.random.rand(5, 5)  # Example 5x5 matrix
Z -= Z.mean(axis=1, keepdims=True)
print(Z)



Z = np.random.randint(0, 10, (5, 5))  # Random 5x5 matrix
n = 2  # Sort by the 3rd column (0-based index)
Z = Z[Z[:, n].argsort()]
print(Z)



Z = np.random.randint(0, 2, (5, 5))  # Random binary matrix
null_columns = np.all(Z == 0, axis=0)
print("Has null columns:", np.any(null_columns))



Z = np.random.rand(10) * 10  # Random array
value = 5
nearest_value = Z[np.abs(Z - value).argmin()]
print("Nearest value to", value, ":", nearest_value)



A = np.array([[1, 2, 3]])
B = np.array([[4], [5], [6]])
C = np.nditer([A, B, None], op_flags=[['readonly'], ['readonly'], ['writeonly']])
for a, b, c in C:
    c[...] = a + b
print(C.operands[2])



class NamedArray(np.ndarray):
    def __new__(cls, array, name="No Name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj

arr = NamedArray([1, 2, 3], name="My Array")
print(arr.name)



Z = np.zeros(10)
indices = [2, 4, 4, 8]  # Example indices (some repeated)
np.add.at(Z, indices, 1)
print(Z)



X = np.array([1, 2, 3, 4, 5])
I = np.array([0, 1, 2, 1, 0])  # Indices
F = np.zeros(3)
np.add.at(F, I, X)
print(F)



image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
unique_colors = np.unique(image.reshape(-1, 3), axis=0)
print("Number of unique colors:", len(unique_colors))



A = np.random.rand(3, 4, 5, 6)
sum_last_two_axes = A.sum(axis=(-2, -1))
print(sum_last_two_axes.shape)  # Should be (3, 4)




D = np.random.rand(10)
S = np.random.randint(0, 3, 10)  # Subset indices
means = [D[S == i].mean() for i in np.unique(S)]
print(means)




A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
diagonal = np.einsum('ij,ji->i', A, B)
print(diagonal)



Z = np.array([1, 2, 3, 4, 5])
Z = np.insert(Z, np.arange(1, Z.size) * 3, 0)
print(Z)



A = np.random.rand(5, 5, 3)
B = np.random.rand(5, 5)
C = A * B[:, :, None]
print(C.shape)  # Should be (5, 5, 3)



Z = np.arange(25).reshape(5, 5)
Z[[0, 1]] = Z[[1, 0]]  # Swap row 0 and row 1
print(Z)



T = np.random.randint(0, 10, (10, 3, 2))  # 10 triangles (each with 3 points)
segments = np.vstack([T[:, [0, 1]], T[:, [1, 2]], T[:, [2, 0]]])
segments = np.sort(segments, axis=1)  # Sort endpoints
unique_segments = np.unique(segments, axis=0)
print(unique_segments)




C = np.array([4, 2, 3])
A = np.repeat(np.arange(len(C)), C)
print(A)  # Should satisfy np.bincount(A) == C




Z = np.arange(10)
window_size = 3
averages = np.convolve(Z, np.ones(window_size)/window_size, mode='valid')
print(averages)




# Create a NumPy array of integers from 1 to 10
arr = np.arange(1, 11)

# Square each element
squared_arr = arr ** 2

# Compute sum, mean, and standard deviation
sum_val = squared_arr.sum()
mean_val = squared_arr.mean()
std_dev = squared_arr.std()

print(f"Squared Array: {squared_arr}")
print(f"Sum: {sum_val}, Mean: {mean_val}, Standard Deviation: {std_dev}")
