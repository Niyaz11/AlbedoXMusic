import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ── Core bot config ────────────────────────────────────────────────────────────
API_ID = ("29245477")
API_HASH = ("0abc83883262245c90ca337b7a0375c4")
BOT_TOKEN = ("8462016049:AAENqxWLz47Voq014jqH4irYCJ43997Hnd8")

OWNER_ID = ("7654385403")
OWNER_USERNAME = ("EternalsHelplineBot")
BOT_USERNAME = ("AlbedoXRobot")
BOT_NAME = ("Albedo Music")
ASSUSERNAME = ("Albedo Assistant"))
EVALOP = list(map(int, getenv("EVALOP", "7654385403").split()))

# ───── Mongo & Logging ───── #
MONGO_DB_URI = ("mongodb+srv://musicxrobot:8Up92WwJbgUS39FV@cluster0.ys1jirt.mongodb.net/")
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
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Niyaz11/AlbedoXMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")

# ───── Support & Community ───── #
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/EternalsHelplineBot")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EternalsHelplineBot")

# ───── Assistant Auto Leave ───── #
AUTO_LEAVING_ASSISTANT = True
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3600"))

# ───── Error Handling ───── #
DEBUG_IGNORE_LOG =True

# ───── Spotify Credentials ───── #
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ───── Session Strings ───── #
STRING1 = "BQG-QCUAokEaPu4bb4O9P59dbo9te5Gyc0K0Cqkrh--op5pGZgiLYqhsTG6Y1_N84u7SCErMr3EPBV184hL1TQOfl6_eH5WGSYokUegnSdGPsKRyBrNNwOalEkbMg695CwI_fquyzpSCg-ScBcNd40OOfI2REmmujpc7z6mzlt2cs83Wd1pfY-hHd3IzxW8g8ZZFIrxUT1A_vHDX7rRz3B2IsZ3dUJUAKRbHfac94IVQ4bZJZHKVYac_TIlReRqkQafDr5sf8wz9ge8NyvSzt5AkAiNeFK1lnParhNdZXZz8ahEE1h-qoArBrMvk449MZBdqYywSUc6iAfkizY8G0_WElIWtlgAAAAFZG6IeAA"
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")



# ───── Bot Media Assets ───── #
START_VIDS = [
    "https://files.catbox.moe/p9kywd.mp4"
]

STICKERS = [
    "CAACAgUAAx0CbtMXSgABAW6caMkVZHh-SOgPD2le3Jj11X3RKHIAAlQcAAJtkUhWuAQct1VGfYkeBA"
]
HELP_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
PING_VID_URL = "https://files.catbox.moe/p9kywd.mp4"
PLAYLIST_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
STATS_VID_URL = "https://files.catbox.moe/p9kywd.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/a8jnkm.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/a8jnkm.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
FAILED = "https://files.catbox.moe/a8jnkm.jpg"


# ───── Utility & Functional ───── #
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")


# ───── Bot Introduction Messages ───── #
AYU = ["💌"]


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
