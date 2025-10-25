import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ── Core bot config ────────────────────────────────────────────────────────────
API_ID = ("29245477")
API_HASH = ("0abc83883262245c90ca337b7a0375c4")
BOT_TOKEN = ("")

OWNER_ID = ("7654385403")
OWNER_USERNAME = ("EternalsHelplineBot")
BOT_USERNAME = ("AlbedoXRobot")
BOT_NAME = ("Albedo Music")
ASSUSERNAME = ("Albedo Assistant"))
EVALOP = list(map(int, getenv("EVALOP", "7654385403").split()))

# ───── Mongo & Logging ───── #
MONGO_DB_URI = ("")
LOGGER_ID = (-1002456565415)

# ── Limits (durations in min/sec; sizes in bytes) ──────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1200"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "157286400"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1288490189"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "30"))

# ── External APIs ──────────────────────────────────────────────────────────────
COOKIE_URL = "https://batbin.me/bractea"  # required (paste link)

API_URL = getenv("")        

API_KEY = getenv("1a853d_YG-HBNXmKh7S3aZOC3Czqa3CuGI7Jh2n")
# ───── Heroku Configuration ───── #
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ───── Git & Updates ───── #
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/CertifiedDevloper/TuneViaBot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")

# ───── Support & Community ───── #
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/EternalsHelplineBot")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EternalsHelplineBot")

# ───── Assistant Auto Leave ───── #
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3600"))

# ───── Error Handling ───── #
DEBUG_IGNORE_LOG =True

# ───── Spotify Credentials ───── #
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ───── Session Strings ───── #
STRING1 = ""
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")



# ───── Bot Media Assets ───── #
START_VIDS = [
    "https://files.catbox.moe/p9kywd.mp4"
]

STICKERS = [
    "CAACAgUAAx0Cd6nKUAACASBl_rnalOle6g7qS-ry-aZ1ZpVEnwACgg8AAizLEFfI5wfykoCR4h4E",
    "CAACAgUAAx0Cd6nKUAACATJl_rsEJOsaaPSYGhU7bo7iEwL8AAPMDgACu2PYV8Vb8aT4_HUPHgQ"
]
HELP_IMG_URL = "https://files.catbox.moe/h3jqa8.jpg"
PING_VID_URL = "https://files.catbox.moe/mi8nr0.mp4"
PLAYLIST_IMG_URL = "https://files.catbox.moe/t72ntd.jpg"
STATS_VID_URL = "https://files.catbox.moe/5vdaw5.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/90juvd.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/7qplwr.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/4roh51.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/wpkxzt.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/cq87ww.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/qp5aa5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/qp5aa5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/qp5aa5.jpg"
FAILED = "https://files.catbox.moe/cq87ww.jpg"


# ───── Utility & Functional ───── #
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")


# ───── Bot Introduction Messages ───── #
AYU = ["💞", "🦋", "🔍", "🧪", "⚡️", "🔥", "🎩", "🌈", "🍷", "🥂", "🥃", "🕊️", "🪄", "💌", "🧨"]


# ───── Runtime Structures ───── #
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ── Minimal validation ─────────────────────────────────────────────────────────
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")

if not COOKIE_URL:
    raise SystemExit("[ERROR] - COOKIE_URL is required.")

# Only allow these cookie link formats
if not re.match(r"^https://(batbin\.me|pastebin\.com)/[A-Za-z0-9]+$", COOKIE_URL):
    raise SystemExit("[ERROR] - Invalid COOKIE_URL. Use https://batbin.me/<id> or https://pastebin.com/<id>")
