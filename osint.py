import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import requests
import re

# === Email Validation ===
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# === Holehe (Social Platform Check) ===
def run_holehe(email):
    try:
        result = subprocess.run(
            ["holehe", email],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stderr and "100%" not in result.stderr:
            return f"⚠️ Holehe Error: {result.stderr.strip()}"
        if not result.stdout.strip():
            return "❌ No social accounts found linked to this email.\n"
        return f"📱 Holehe:\n{result.stdout.strip()}\n"
    except Exception as e:
        return f"❌ Holehe failed: {e}\n"

# === EmailRep.io API Check ===
def check_emailrep(email):
    try:
        resp = requests.get(f"https://emailrep.io/{email}", timeout=5)
        if resp.status_code != 200:
            return "⚠️ EmailRep.io Error: Invalid response.\n"
        data = resp.json()
        summary = f"""📊 EmailRep.io:
Reputation: {data.get('reputation', 'N/A')}
Suspicious: {data.get('suspicious', 'N/A')}
Blacklisted: {data.get('blacklisted', 'N/A')}
Domain: {data.get('details', {}).get('domain', 'N/A')}
Disposable: {data.get('details', {}).get('disposable', 'N/A')}
Malicious Activity: {data.get('details', {}).get('malicious_activity', 'N/A')}
"""
        return summary + "\n"
    except Exception as e:
        return f"❌ EmailRep.io failed: {e}\n"

# === HaveIBeenPwned Breach Check ===
def check_hibp(email):
    headers = {"User-Agent": "OSINT-Tool"}
    try:
        resp = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", headers=headers, timeout=5)
        if resp.status_code == 404:
            return "✅ No breaches found on HaveIBeenPwned.\n"
        elif resp.status_code == 200:
            breaches = [b["Name"] for b in resp.json()]
            return f"🔐 HaveIBeenPwned:\nBreached in: {', '.join(breaches)}\n"
        elif resp.status_code == 403:
            return "⚠️ HIBP API key required for access.\n"
        else:
            return "⚠️ Unexpected response from HaveIBeenPwned.\n"
    except Exception as e:
        return f"❌ HIBP check failed: {e}\n"

# === Run All Scans ===
def run_all_checks():
    output_box.delete(1.0, tk.END)
    email = input_entry.get().strip()

    if not is_valid_email(email):
        output_box.insert(tk.END, "❌ Please enter a valid email address.\n")
        return

    output_box.insert(tk.END, f"🔍 Scanning: {email}\n\n")
    root.update()

    output_box.insert(tk.END, check_emailrep(email))
    root.update()

    output_box.insert(tk.END, check_hibp(email))
    root.update()

    output_box.insert(tk.END, run_holehe(email))
    root.update()

# === GUI Setup ===
root = tk.Tk()
root.title("🔍 OSINT Email Intelligence Scanner")
root.geometry("850x600")
root.configure(bg="#0f0f0f")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="#00ff00", background="#202020", padding=10, font=("Consolas", 12, "bold"))
style.configure("TEntry", foreground="#00ff00", fieldbackground="#1e1e1e", background="#1e1e1e", font=("Consolas", 12))
style.configure("TLabel", foreground="#00ff00", background="#0f0f0f", font=("Consolas", 14, "bold"))

header = ttk.Label(root, text="🕵️ OSINT Email Intelligence Tool", anchor="center")
header.pack(pady=10)

input_frame = tk.Frame(root, bg="#0f0f0f")
input_frame.pack(pady=10)

input_label = ttk.Label(input_frame, text="Email Address:")
input_label.pack(side=tk.LEFT, padx=5)

input_entry = ttk.Entry(input_frame, width=40)
input_entry.pack(side=tk.LEFT, padx=5)

search_button = ttk.Button(input_frame, text="Run OSINT", command=run_all_checks)
search_button.pack(side=tk.LEFT, padx=5)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 12))
output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
