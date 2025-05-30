
import math
import re
import tkinter as tk
from tkinter import messagebox

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password):
        charset += 32  # Approximate special characters
    if charset == 0:
        return 0
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def check_length_complexity(password):
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password)
    return {
        "length_ok": length_ok,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special
    }

def regex_validation(password):
    patterns = {
        "Uppercase": r"[A-Z]",
        "Lowercase": r"[a-z]",
        "Digit": r"\d",
        "Special Char": r"[!@#$%^&*(),.?\":{}|<>]"
    }
    results = {}
    for name, pattern in patterns.items():
        results[name] = bool(re.search(pattern, password))
    return results

def evaluate_password():
    pwd = entry.get()
    entropy = calculate_entropy(pwd)
    complexity = check_length_complexity(pwd)
    regex_result = regex_validation(pwd)

    strength = "Weak"
    if entropy > 60 and all(complexity.values()):
        strength = "Strong"
    elif entropy > 40:
        strength = "Moderate"

    result_text = f"Entropy: {entropy} bits\nStrength: {strength}\n\n"
    result_text += "Complexity:\n"
    for k, v in complexity.items():
        result_text += f"  {k.replace('_', ' ').title()}: {'✔️' if v else '❌'}\n"

    result_text += "\nRegex Check:\n"
    for k, v in regex_result.items():
        result_text += f"  {k}: {'✔️' if v else '❌'}\n"

    messagebox.showinfo("Password Evaluation", result_text)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=evaluate_password).pack(pady=10)

root.mainloop()
