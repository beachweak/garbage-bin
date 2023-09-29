import tkinter as tk
import random
import string

# Function to generate random debug information
def generate_debug_info():
    debug_labels = [
        "user_location",
        "payment_method",
        "server_response_time",
        "authentication_status",
        "data_validation",
        "transaction_id",
        "error_code",
        "hardware_sensor_reading",
        "user_interaction",
        "algorithm_step",
        "environment_variable",
        "battery_level",
        "notification_status",
        "resource_usage",
        "input_validation",
        "debug_trace",
        "email_delivery",
        "queue_length",
        "database_connection",
        "service_status",
        "third_party_integration",
        "log_message",
        "data_migration",
        "user_preferences",
        "permission_check"
    ]
    debug_info = "\n".join([f"{random.choice(debug_labels)}: {random.uniform(0, 100):.2f}" for _ in range(15)])
    return debug_info

# Function to generate random Yes or No
def generate_yes_no():
    yes_no_labels = [
        "error_occurred",
        "debug_enabled",
        "security_violation",
        "data_corruption",
        "performance_issue",
        "syro",
        "aphex_twin",
        "cornwall",
        "rdj",
        "error_occurred",
        "debug_enabled",
        "security_violation",
        "data_corruption",
        "performance_issue",
        "error_occurred",
        "debug_enabled",
        "security_violation",
        "data_corruption",
        "performance_issue",
        "error_occurred",
        "debug_enabled",
        "security_violation",
        "data_corruption",
        "performance_issue"
    ]
    return random.choice(yes_no_labels)

# Function to update the debug information label
def update_debug_label():
    debug_info = generate_debug_info()
    yes_no_info = "\n".join([f"{generate_yes_no()}: {random.choice(['Yes', 'No'])}" for _ in range(10)])
    debug_label.config(text=f"{debug_info}\n\n{yes_no_info}")
    root.after(200, update_debug_label)  # Update every 200 milliseconds

# Create the main tkinter window
root = tk.Tk()
root.title("Random Debug Info")
root.geometry("1000x1000")
root.configure(bg="#000000")  # Set background color to #000000

# Create a label to display the debug information
debug_label = tk.Label(root, text="", fg="#CAD400", bg="#000000", font=("Helvetica", 12), justify="left")
debug_label.pack(padx=20, pady=20, anchor="nw")  # Position on the left side

# Start updating the debug information
update_debug_label()

# Start the tkinter main loop
root.mainloop()
