# TimeButler AutoClock-In

![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue)
![Python](https://img.shields.io/badge/python-3.14-blue?logo=python)
![License](https://img.shields.io/badge/license-AGPLv3-blue)
![Requirements](https://img.shields.io/badge/dependencies-pip--requirements-blue)

A Python script that automatically clocks you in on [TimeButler](https://timebutler.de) at login — once per day.

---

## 🚀 Features

- Automatically clocks in on TimeButler at system startup.
- Runs once per day — safe to have multiple logins or reboots.
- Reads credentials from a `.env` file — no hardcoded secrets.
- Works on macOS (launchd) and Linux (systemd).

---

## 📁 Project Structure

```
AutoStart-TimeButler/
├── clock_in.py       # Main script
├── .env              # Credentials (not committed)
├── .env.example      # Template for .env
└── requirements.txt  # Python dependencies
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/jaherhum/autostart-timebutler.git
cd autostart-timebutler
```

### 2. Install Python 3.14

**macOS:**
```bash
brew install python@3.14
```

**Linux:**
```bash
sudo apt install python3.14        # Debian/Ubuntu
sudo pacman -S python              # Arch
sudo dnf install python3.14        # Fedora
```

### 3. Create the virtual environment and install dependencies

```bash
python3.14 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 4. Configure credentials

```bash
cp .env.example .env
```

Edit `.env` with your TimeButler credentials:

```env
TIMEBUTLER_USER=your@email.com
TIMEBUTLER_PASSWORD=yourpassword
```

---

## 🧩 Usage

Run manually to verify everything works before setting up autostart:

```bash
.venv/bin/python clock_in.py
```

---

- **macOS** — create a [Launch Agent (launchd)](https://support.apple.com/guide/terminal/apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac)
- **Linux** — create a [systemd user service](https://wiki.archlinux.org/title/Systemd/User)

---

## 🐞 Issues

Please open an issue if you find any problems or unexpected behavior.

---

## 📜 License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

📄 [Read the full license](https://www.gnu.org/licenses/agpl-3.0.html)

---

## 🙌 Credits

Made by **Jaherhum**.