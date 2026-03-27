"""
Auto clock-in script for Timebutler.
"""
import sys
import os
from dotenv import load_dotenv
import requests
import time
from pathlib import Path
from datetime import date

load_dotenv()
session = requests.Session()

# ─────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────

BASE_URL = os.getenv("BASE_URL", "https://app.timebutler.com/")
USER_EMAIL = os.getenv("USER_EMAIL", "")
USER_PASSWORD = os.getenv("USER_PASSWORD", "")
DELAY_BETWEEN_REQUESTS = float(os.getenv("DELAY_BETWEEN_REQUESTS", "0.3"))

def login():
    """Logs into Timebutler."""
    print("Logging into Timebutler...")
    response = session.get(
        "https://app.timebutler.com/do",
        params={
            "ha": "login",
            "ac": 1,
            "afteroauth": 0,
            "login": USER_EMAIL,
            "passwort": USER_PASSWORD,
            "keeplogin": 1,
        }
    )


def clock_in():
    """Clocks-in."""
    response = session.get(
        "https://app.timebutler.com/do",
        params={
            "ha": "zee",
            "ac": 101,
            "compid": "",
            "ajx": 1,
            "_": int(time.time() * 1000)  # timestamp en ms
        }
    )
    response.raise_for_status()

    data = response.json()

    if not data["payload"][0]["running"]:
        raise RuntimeError(f"Clock-in failed: {data}")


def main():
    # ── 0. Validates .env values ─────────────────────────
    if not USER_EMAIL:
        raise ValueError("USER_EMAIL must be set.")
    if not USER_PASSWORD:
        raise ValueError("USER_PASSWORD must be set.")

    try:

        # ── 1. Checks if the script has run before today. ─────────────────────────
        STAMP = Path(__file__).parent / ".last_run"

        today = str(date.today())
        if STAMP.exists() and STAMP.read_text().strip() == today:
            sys.exit(0)

        # ── 1. Logs in ─────────────────────────
        login()
        print("Successfully logged in.")
        time.sleep(DELAY_BETWEEN_REQUESTS)
        # ── 2. Clocks in ─────────────────────────
        clock_in()
        print("Successfully clocked in.")

        # ── Creates a file with today's date to avoid re-clocking in. ─────────────────────────
        STAMP.write_text(today)

    except RuntimeError as e:
        print(f"Error: {e}")
    except requests.HTTPError as e:
        print(f"HTTP Error: {e}")


if __name__ == "__main__":
    main()
    sys.exit(0)