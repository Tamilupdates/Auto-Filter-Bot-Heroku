from requests import get as rget
import os

CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL')
try:
    if len(CONFIG_FILE_URL) == 0:
        raise TypeError
    try:
        res = rget(CONFIG_FILE_URL)
        if res.status_code == 200:
            with open('info.py', 'wb+') as f:
                f.write(res.content)
        else:
            LOGGER.error(f"Failed to download info.py {res.status_code}")
    except Exception as e:
        LOGGER.error(f"CONFIG_FILE_URL: {e}")
except Exception as e:
    LOGGER.error(e)
    pass
