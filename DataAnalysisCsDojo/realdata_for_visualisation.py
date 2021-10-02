import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('countries.csv')
print(data)

# Compare population growth between US and China
us = data[data.country == 'United States']
print(us)

china = data[data.country == 'China']
print(china)

pop = plt.figure(1)
plt.plot(us.year, us.population / 10**6) # Display pop in millions, divide whole pop with 1 million: 10**6
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.title("Population against Year")
 
# Show relative growth in population with percentage
print(us.population / us.population.iloc[0] * 100) # divide by the first year

pop_percent = plt.figure(2)
plt.plot(us.year, us.population / us.population.iloc[0] * 100) # Display pop in millions, divide whole pop with 1 million: 10**6
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population growth (first year = 100)')
plt.title("Population growth against Year")

plt.show()
