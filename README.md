# TimeButler AutoClock-In

![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue)
![Python](https://img.shields.io/badge/python-3.11%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-blue)
![Dependencies](https://img.shields.io/badge/dependencies-uv--inline-blue)

A Python script that automatically clocks you in on [TimeButler](https://timebutler.de) at login — once per day.

---

## 🚀 Features

- Automatically clocks in on TimeButler at system startup.
- Runs once per day — safe to have multiple logins or reboots.
- Reads credentials from a `.env` file — no hardcoded secrets.
- Uses [uv](https://docs.astral.sh/uv/) for zero-setup dependency management.
- Works on macOS (launchd) and Linux (systemd).

---

## 📁 Project Structure
```
timebutler-autoclock-in/
├── clock_in.py    # Main script (inline dependencies via uv)
├── .env           # Credentials (not committed)
└── .env.example   # Template for .env
```

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/jaherhum/autostart-timebutler.git
cd autostart-timebutler
```

### 2. Install uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> uv will automatically download the required Python version and resolve dependencies on first run. No virtual environment setup needed.

### 3. Configure credentials
```bash
cp .env.example .env
```

Edit `.env` with your TimeButler credentials:
```env
USER_EMAIL=your@email.com
USER_PASSWORD=yourpassword
```

---

## 🧩 Usage

Run manually to verify everything works before setting up autostart:
```bash
./clock_in.py
```

Or explicitly with uv:
```bash
uv run clock_in.py
```

---

- **macOS** — create a [Launch Agent (launchd)](https://support.apple.com/guide/terminal/apdc6c1077b-5d5d-4d35-9c19-60f2397b2369/mac)
- **Linux** — create a [systemd user service](https://wiki.archlinux.org/title/Systemd/User)

---

## 🐞 Issues

Please open an issue if you find any problems or unexpected behavior.

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

📄 [Read the full license](./LICENSE)

---

## 🙌 Credits

Made by **Jaherhum**.
