import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

world_health_data = pd.read_csv(r"C:\Users\Dakshina\Downloads\Causes Of Death.csv")

print(world_health_data.head())
print(world_health_data.describe())

print(world_health_data.isnull().sum())
world_health_data['Entity'] = world_health_data['Entity'].replace(['America', 'United States'], 'USA')

total_deaths_by_cause = world_health_data.groupby('Causes name')['Death Numbers'].sum().reset_index()
#Sorting the deaths by cause in descending order
total_deaths_by_cause_sorted = total_deaths_by_cause.sort_values(by='Death Numbers', ascending=False)
#Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x='Death Numbers', y='Causes name', data=total_deaths_by_cause_sorted, orient='h')
plt.xlabel('Total Deaths')
plt.ylabel('Cause')
plt.title('Total Deaths by Cause', fontdict={'fontsize': 16, 'fontweight': 'bold'})
plt.show()




# Creating a pivot table to summarize the data by year
pivot_table = world_health_data.pivot_table(index='Year', values='Death Numbers', aggfunc='sum')

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(pivot_table.index, pivot_table.values, marker='o', color='g', label='Total Deaths')
plt.xlabel('Year')
plt.ylabel('Deaths(in millions)')
plt.title('Total Deaths by Year', fontdict={'fontsize': 16, 'fontweight': 'bold'})
plt.grid(True)
plt.legend()
plt.show()

# Displaying the pivot table
print(pivot_table)