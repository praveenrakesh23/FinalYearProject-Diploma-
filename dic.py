import sqlite3
import matplotlib.pyplot as plt

custom_colors = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45"]
# Initialize a dictionary to store the day counts
date_list = {"Sunday": 0, "Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0}

# Connect to the SQLite database
with sqlite3.connect("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db") as db:
    cur = db.cursor()
    query2 = "SELECT Day FROM bill"
    cur.execute(query2)
    dates = cur.fetchall()

    # Loop through the fetched dates and update the counts in the dictionary
    for date in dates:
        day = date[0]  # Extract the day from the fetched data
        if day in date_list:
            date_list[day] += 1



# Data from the date_list dictionary
days = list(date_list.keys())
counts = list(date_list.values())

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.scatter(days, counts, color = custom_colors)
plt.plot(days, counts)
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Bills Generated', fontsize=14)
plt.title("Sales done in Week Days")


# Show the plot
plt.show()
