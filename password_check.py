import tkinter as tk
from tkinter import messagebox

def check_password(password):

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    special_chars = "!@#$%^&*(),.?\":{}|<>"


    if len(password) < 8:
        return "The length of the password must be at least 8 characters long"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if not has_upper:
        return "Password must contain at least one uppercase letter. Please try again"
    if not has_lower:
        return "Password must contain at least one lowercase letter. Please try again"
    if not has_digit:
        return "Password must contain at least one number. Please try again"
    if not has_special:
        return "Password must contain at least one special character. Please try again"
    
    return "Strong: Your password is secure!"

def on_check_password():
    password = entry.get()
    result = check_password(password)
    messagebox.showinfo("Password Check Result", result)
    if result.startswith("Strong"):
        root.quit()

# Create the GUI application
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.configure(bg="#2c3e50")

tk.Label(root, text="Enter your password:", font=("Arial", 12, "bold"), bg="#2c3e50", fg="white").pack(pady=10)
entry = tk.Entry(root, show="*", font=("Arial", 12), width=30, bd=2, relief="groove")
entry.pack(pady=5)

tk.Button(root, text="Check Password", command=on_check_password, font=("Arial", 12, "bold"), bg="#27ae60", fg="white", activebackground="#2ecc71", activeforeground="white", padx=10, pady=5, bd=2, relief="raised").pack(pady=15)

root.mainloop()


