import tkinter as tk
from tkinter import messagebox

# Create a function to send an email (placeholder)
def send_email():
    messagebox.showinfo("Email Sent", "Your email has been sent successfully!")

# Create the main application window
app = tk.Tk()
app.title("Mail Application")

# Create and configure widgets (labels, entry fields, buttons, etc.)
subject_label = tk.Label(app, text="Subject:")
subject_entry = tk.Entry(app, width=40)
message_label = tk.Label(app, text="Message:")
message_text = tk.Text(app, width=40, height=10)
send_button = tk.Button(app, text="Send Email", command=send_email)

# Arrange widgets on the GUI using the grid layout manager
subject_label.grid(row=0, column=0, padx=10, pady=5)
subject_entry.grid(row=0, column=1, padx=10, pady=5)
message_label.grid(row=1, column=0, padx=10, pady=5)
message_text.grid(row=1, column=1, padx=10, pady=5)
send_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI application
app.mainloop()
