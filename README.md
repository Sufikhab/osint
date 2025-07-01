# 🕵️‍♂️ OSINT Email Intelligence Scanner (GUI)

A sleek Python-based **GUI tool** for performing Open Source Intelligence (OSINT) on email addresses.  
It gathers information from public sources like:

- 🔍 [EmailRep.io](https://emailrep.io)
- 🔐 [HaveIBeenPwned](https://haveibeenpwned.com)
- 👤 [Holehe](https://github.com/megadose/holehe) – checks if the email is registered on various platforms

Built with **Tkinter**, this desktop tool offers a modern green-on-black theme and real-time scan output.

---

## ⚙️ Features

- 📬 Validate and scan email addresses
- 📊 Check email reputation and risk using EmailRep.io
- 🔐 Detect data breaches using HaveIBeenPwned
- 👁️ Scan 40+ platforms for email existence using Holehe
- 🖥️ Interactive GUI with dark theme and live output updates

---

## 🧩 Requirements

Install required Python packages:

```bash
pip install requests colorama
```

You must also install **Holehe**:

```bash
pip install holehe
```

> Ensure `holehe` is accessible from your system terminal (`holehe user@example.com`)

---

## 🚀 Running the Tool

```bash
python osint.py
```

You will see a GUI window where you can enter an email address and run an OSINT scan.

---

## 🖼️ GUI Preview

- Entry box for email address  
- "Run OSINT" button  
- Scrollable output area  
- All scan results printed in real-time

---

## 🧪 Sample Output

```
🔍 Scanning: user@example.com

📊 EmailRep.io:
Reputation: suspicious
Suspicious: True
Blacklisted: True
Domain: example.com
Disposable: False
Malicious Activity: True

🔐 HaveIBeenPwned:
Breached in: Adobe, LinkedIn

📱 Holehe:
[+] Twitter: FOUND
[+] Facebook: FOUND
```

---

## ❗ API Access

- **EmailRep.io** is free for basic use (limited rate)
- **HaveIBeenPwned** may require an API key for frequent or advanced usage

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Suggestions, bug reports, and pull requests are welcome!

---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub and share it with your fellow OSINT investigators!

