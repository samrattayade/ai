import matplotlib.pyplot as plt

# Sample data
x = ['Python', 'Java', 'C++', 'JavaScript']
y = [80, 65, 70, 90]

# Create bar chart
plt.bar(x, y, color='skyblue')

# Add labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity Score')
plt.title('Programming Language Popularity')

# Show chart
plt.show()
