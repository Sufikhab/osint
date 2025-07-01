# 🕵️‍♂️ OSINT Information Gathering Tool

An advanced Python-based **OSINT (Open Source Intelligence)** tool for gathering and correlating data from public sources.

Supports scanning emails, usernames, IP addresses, and phone numbers using powerful APIs and tools like **EmailRep.io**, **HaveIBeenPwned**, **Nmap**, **Sherlock**, and **PhoneInfoga**.

---

## 🚀 Features

- 🔍 Email reputation checks via [EmailRep.io](https://emailrep.io)
- 🕳️ Credential leak checks via [HaveIBeenPwned](https://haveibeenpwned.com)
- 👤 Username checks across 300+ platforms using **Sherlock**
- 📞 Phone number OSINT using **PhoneInfoga**
- 🌐 IP analysis with `nmap`
- 🧠 AI-powered data correlation engine (optional enhancement)

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/osint-tool.git
cd osint-tool
```

### 2. Create and activate a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install requests colorama
```

---

## 🔧 Install External Tools

### 🛠 Nmap

Download & install from: https://nmap.org/download.html  
Make sure it's accessible in your terminal:

```bash
nmap --version
```

### 🕵 Sherlock (for username search)

```bash
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
pip install -r requirements.txt
python3 sherlock.py username
```

### 📞 PhoneInfoga (for phone OSINT)

Recommended via Docker:

```bash
docker pull sundowndev/phoneinfoga
```

Or install manually: https://github.com/sundowndev/phoneinfoga

---

## 🧪 Usage

```bash
python osint.py
```

You will be prompted to enter:

- Email address, username, IP, or phone number
- Scan type
- View live OSINT results

---

## 🔍 Sample Output

```
[+] Email: user@example.com
  - Reputation: suspicious
  - Leaked in 2 breaches
  - Disposable: No

[+] Username: hackerX
  - Found on: GitHub, Reddit, Twitter

[+] Phone: +14155552671
  - Country: United States
  - Carrier: Verizon
  - Format: Valid

[+] IP: 192.168.1.1
  - Open Ports: [22, 80]
```
---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome!  
Submit a pull request or open an issue to improve this tool.

---

## ⭐ Show Support

If this helped your recon workflow, consider giving it a ⭐ on GitHub!

