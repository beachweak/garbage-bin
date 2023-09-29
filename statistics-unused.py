import tkinter as tk
import random
import time

# Function to generate fake statistics
def generate_fake_stats():
    fake_stats = {
        "Stat 1": random.randint(1, 1000),
        "Stat 2": random.uniform(0, 1),
        "Stat 3": random.randint(10000, 20000),
        "Stat 4": random.randint(500, 1000),
        "Stat 5": random.uniform(10, 50),
    }
    return fake_stats

# Function to update statistics label
def update_statistics_label():
    fake_stats = generate_fake_stats()
    stats_label.config(text="\n".join([f"{key}: {value}" for key, value in fake_stats.items()]))
    root.after(1000, update_statistics_label)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Fake Statistics")

# Create a label to display fake statistics
stats_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
stats_label.pack(side="right", fill="both", expand=True)

# Start updating the statistics label
update_statistics_label()

# Start the Tkinter main loop
root.mainloop()
