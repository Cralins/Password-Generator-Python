import random
import string
import tkinter as tk

def generate_password():
    # Set the password length to 18 characters
    password_length = 18
    
    # Combine all suitable character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Determine the number of characters required to have at least one uppercase letter, one lowercase letter, one digit,
    #  and one special character in the password
    num_uppercase = 1
    num_lowercase = 1
    num_digits = 1
    num_special = 1
    
    # Select the required characters
    uppercase_characters = string.ascii_uppercase
    password = "".join(random.choices(uppercase_characters, k=num_uppercase))
    
    lowercase_characters = string.ascii_lowercase
    password += "".join(random.choices(lowercase_characters, k=num_lowercase))
    
    digits = string.digits
    password += "".join(random.choices(digits, k=num_digits))
    
    special_characters = string.punctuation
    password += "".join(random.choices(special_characters, k=num_special))
    
    # Select the remaining characters randomly
    password += "".join(random.choices(characters, k=password_length - len(password)))
    
    return password

def refresh_password():
    password_display['text'] = generate_password()

def copy_password():
    root.clipboard_clear()
    password = password_display['text']
    root.clipboard_append(password)

def close_window():
    root.destroy()

# Create a pop-up window
root = tk.Tk()
root.title("Password Generator")
root.geometry("280x80")

# Password label
password_label = tk.Label(root, text="Password:")
password_label.pack()

# Password display field
password_display = tk.Label(root, text=generate_password(), font=("Courier New", 14))
password_display.pack()

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Refresh button
refresh_button = tk.Button(button_frame, text="Refresh", command=refresh_password, width=10)
refresh_button.pack(side=tk.LEFT, padx=5)

# Copy button
copy_button = tk.Button(button_frame, text="Copy", command=copy_password, width=10)
copy_button.pack(side=tk.LEFT, padx=5)

# Close button
close_button = tk.Button(button_frame, text="Close", command=close_window, width=10)
close_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
