import os
import logging
import asyncio
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from dotenv import load_dotenv

LOG_FILE_NAME = "Encoder@Log.txt"

if os.path.exists(LOG_FILE_NAME):
    with open(LOG_FILE_NAME, "r+") as f_d:
        f_d.truncate(0)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=2097152000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
LOGS = logging.getLogger(__name__)


THUMB = "https://te.legra.ph/file/2ebf402cdef8c27ab4648.jpg"
os.system(f"wget {THUMB} -O thumb.jpg")
ffmpeg = []
ffmpeg.append("-map 0 -c:v libx265 -crf 24 -c:s copy  -s 1280x720 -preset veryfast -c:a libopus -ab 60k -vbr 2 -ac 2 -level 2.1")
try:
 api_id = int(os.environ.get("12183504"))
 api_hash = os.environ.get("e8940ffd7acc09622c404b9e42d3aacb")
 bot_token = os.environ.get("5278800567:AAGfqbMu3ZbTeJTfocP2EDV8oDdIT7pbzkE")
 DATABASE_URL = os.environ.get("DATABASE_URL") 
 BOT_USERNAME = "Prem_Hulk32_bot"
 MAX_MESSAGE_LENGTH = 4096
 download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
 sudo_users = list(set(int(x) for x in os.environ.get("5137809317").split()))
 sudo_users.append(1099725030)
 sudo_users.append(5089884151)
 LOG_CHANNEL = os.environ.get("prembotlogs")
except Exception as e:
 LOGS.info("ENV Are Missing")

app = Client("nirusaki", api_id=api_id, api_hash=api_hash, bot_token=bot_token, workers=2)
0
data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
