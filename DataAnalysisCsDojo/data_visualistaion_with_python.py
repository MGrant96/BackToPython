import pandas as pd
from matplotlib import pyplot as plt

# x = [1, 2, 3]
# y = [1, 4, 9]
# z = [10, 5, 0]
# plt.plot(x, y)
# plt.plot(x, z)
# plt.title("Test Plot")
# plt.xlabel("x")
# plt.ylabel("y and z")
# plt.legend(["This is y", "This is z"])
# plt.show()

sample_data = pd.read_csv('sample_data.csv')
print(sample_data)
print(type(sample_data))

print(sample_data.column_c)
print(type(sample_data.column_c))

print(sample_data.column_c.iloc[1])
print(sample_data.column_c.iloc[2])

# plot col a on x axis and col b on y
plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c)

plt.show()













