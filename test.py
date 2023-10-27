import matplotlib.pyplot as plt
import sqlite3

# Create a Matplotlib figure with 6 rows and 1 column
fig, ax = plt.subplots(figsize=(14.21, 8))

with sqlite3.connect("sqlite.db") as db:
    cur = db.cursor()
    # Fetch both product names and amounts
    query = "SELECT product_name, amount FROM anal"
    cur.execute(query)
    data = cur.fetchall()

    # Extract the product names and amounts into separate lists
    product_names = [item[0] for item in data]
    amounts = [item[1] for item in data]

    # Sort by amounts and select the top 7
    sorted_data = sorted(zip(product_names, amounts), key=lambda x: x[1], reverse=True)  # Sort in descending order
    x_top_7 = [item[0] for item in sorted_data[:7]]
    y_top_7 = [item[1] for item in sorted_data[:7]]


    # Plot the data as a line
    ax.plot(product_names, amounts, label='Line Plot', marker='o', linestyle='-', color='b')

    # Add labels and a legend
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Simple Line Plot')
    ax.legend()

    # Show the plot
    plt.show()
