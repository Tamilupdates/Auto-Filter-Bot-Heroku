import logging
from requests import get as rget
import os

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)

CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL')
try:
    if not CONFIG_FILE_URL:
        raise ValueError("CONFIG_FILE_URL is missing or empty")

    res = rget(CONFIG_FILE_URL)
    if res.status_code == 200:
        with open('info.py', 'wb+') as f:
            f.write(res.content)
    else:
        LOGGER.error(f"Failed to download info.py {res.status_code}")
except Exception as e:
    LOGGER.error(f"Error downloading CONFIG_FILE_URL: {e}")

UTILS_FILE_URL = os.environ.get('UTILS_FILE_URL')
if UTILS_FILE_URL:  # Check if UTILS_FILE_URL is provided
    try:
        res = rget(UTILS_FILE_URL)
        if res.status_code == 200:
            with open('utils.py', 'wb+') as f:
                f.write(res.content)
        else:
            LOGGER.error(f"Failed to download utils.py {res.status_code}")
    except Exception as e:
        LOGGER.error(f"Error downloading UTILS_FILE_URL: {e}")
else:
    LOGGER.info("UTILS_FILE_URL not provided. Skipping download.")
