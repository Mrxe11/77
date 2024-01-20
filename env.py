import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "29914850").strip()
API_HASH = os.getenv("API_HASH", "de7b0ee6f49fff7b4a5f0e5c015972ce").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6637654605:AAEgIigaPwPrlP2iqHIbnZsJ5b7PojAMD08").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
