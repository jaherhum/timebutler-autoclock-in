#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
#   "python-dotenv",
#   "plyer",
#   "pyobjus"; sys_platform == 'darwin'",
# ]
# ///

"""
Auto clock-in script for Timebutler.
"""
import sys
import os
from dotenv import load_dotenv
from plyer import notification
import requests
import time
from pathlib import Path
from datetime import date

load_dotenv()
session = requests.Session()

# ─────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────

BASE_URL = os.getenv("BASE_URL", "https://app.timebutler.com")
USER_EMAIL = os.getenv("USER_EMAIL", "")
USER_PASSWORD = os.getenv("USER_PASSWORD", "")
DELAY_BETWEEN_REQUESTS = float(os.getenv("DELAY_BETWEEN_REQUESTS", "0.3"))


# ─────────────────────────────────────────────
#  NOTIFICATIONS
# ─────────────────────────────────────────────

def notify(title: str, message: str):
    try:
        notification.notify(title=title, message=message, app_name="Timebutler", timeout=5)
    except Exception:
        pass

# ─────────────────────────────────────────────
#  FUNCTIONS
# ─────────────────────────────────────────────

def login():
    """Logs into Timebutler."""
    response = session.get(
        f"{BASE_URL}/do",
        params={
            "ha": "login",
            "ac": 1,
            "afteroauth": 0,
            "login": USER_EMAIL,
            "passwort": USER_PASSWORD,
            "keeplogin": 1,
        }
    )
    response.raise_for_status()

    if "pp" not in session.cookies:
        raise RuntimeError("Login failed: wrong credentials.")


def clock_in():
    """Clocks-in."""
    response = session.get(
        f"{BASE_URL}/do",
        params={
            "ha": "zee",
            "ac": 101,
            "compid": "",
            "ajx": 1,
            "_": int(time.time() * 1000)
        }
    )
    response.raise_for_status()

    data = response.json()

    if not data["payload"][0]["running"]:
        raise RuntimeError(f"Clock-in failed: {data}")


def main():
    try:
        # ── 0. Validates .env values ─────────────────────────
        if not USER_EMAIL:
            raise ValueError("USER_EMAIL must be set.")
        if not USER_PASSWORD:
            raise ValueError("USER_PASSWORD must be set.")

        # ── 1. Checks if the script has run before today ─────────────────────────
        STAMP = Path(__file__).parent / ".last_run"
        today = str(date.today())
        if STAMP.exists() and STAMP.read_text().strip() == today:
            notify("Clock-in", "Already clocked in today, skipping.")
            sys.exit(0)

        # ── 2. Logs in ─────────────────────────
        print("Logging into Timebutler...")
        login()
        print("Successfully logged in.")
        time.sleep(DELAY_BETWEEN_REQUESTS)

        # ── 3. Clocks in ─────────────────────────
        clock_in()
        print("Successfully clocked in.")
        notify("Clock-in", "Clock-in successful!")

        # ── 4. Stamps today's date to avoid re-clocking in ─────────────────────────
        STAMP.write_text(today)

    except ValueError as e:
        msg = f"Config Error: {e}"
        print(msg)
        notify("Clock-in Error", msg)

    except RuntimeError as e:
        msg = f"Error: {e}"
        print(msg)
        notify("Clock-in Error", msg)

    except requests.HTTPError as e:
        msg = f"HTTP Error: {e}"
        print(msg)
        notify("Clock-in Error", msg)


if __name__ == "__main__":
    main()
    sys.exit(0)