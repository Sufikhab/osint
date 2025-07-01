import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import re

# === Email Validation ===
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# === Run Holehe ===
def run_holehe(email):
    try:
        result = subprocess.run(
            ["holehe", email],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Filter tqdm progress output from stderr
        if result.stderr and "100%" not in result.stderr:
            return f"⚠️ Error: {result.stderr.strip()}"

        if not result.stdout.strip():
            return "❌ No social accounts found linked to this email."

        return result.stdout.strip()

    except Exception as e:
        return f"❌ Holehe failed to run: {e}"


# === GUI Trigger ===
def run_lookup():
    output_box.delete(1.0, tk.END)
    email = input_entry.get().strip()
    if not is_valid_email(email):
        output_box.insert(tk.END, "❌ Please enter a valid email address.\n")
        return

    output_box.insert(tk.END, f"🔍 Running holehe on: {email}\n\n")
    output_box.insert(tk.END, "⌛ Please wait, scanning platforms...\n\n")
    root.update()

    output = run_holehe(email)
    output_box.insert(tk.END, output)

# === GUI Setup ===
root = tk.Tk()
root.title("🔍 OSINT Email Scan (holehe)")
root.geometry("800x600")
root.configure(bg="#0f0f0f")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="#00ff00", background="#202020", padding=10, font=("Consolas", 12, "bold"))
style.configure("TEntry", foreground="#00ff00", fieldbackground="#1e1e1e", background="#1e1e1e", font=("Consolas", 12))
style.configure("TLabel", foreground="#00ff00", background="#0f0f0f", font=("Consolas", 14, "bold"))

header = ttk.Label(root, text="💻 OSINT Tool - Email Social Media Scanner (holehe)", anchor="center")
header.pack(pady=10)

input_frame = tk.Frame(root, bg="#0f0f0f")
input_frame.pack(pady=10)

input_label = ttk.Label(input_frame, text="Email Address:")
input_label.pack(side=tk.LEFT, padx=5)

input_entry = ttk.Entry(input_frame, width=40)
input_entry.pack(side=tk.LEFT, padx=5)

search_button = ttk.Button(input_frame, text="Scan", command=run_lookup)
search_button.pack(side=tk.LEFT, padx=5)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 12))
output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
