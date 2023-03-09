# v1

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '14553761'))                                 # Recommended
API_HASH = environ.get('API_HASH', 'a1cab49dcdfd2eb3bea5e5a552c5d479')          # Recommended
BOT_TOKEN = environ.get('BOT_TOKEN', "")                                        # Recommended

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', '')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '604152966').split()]    # Recommended
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
updates_channel = environ.get('UPDATES_CHANNEL', '')                            # Make admin on this bot your channel
auth_grp = environ.get('AUTH_GROUP', '')
UPDATES_CHANNEL = int(updates_channel) if updates_channel and id_pattern.search(updates_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "")                                  # Recommended
DATABASE_NAME = environ.get('DATABASE_NAME', "Filterbot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegramfiles')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))                               # Recommended
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Nanthakps')                         # Recommended
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION",
'''<b>
🗂️ File : {file_name}

🏷 Size : {file_size}

📥 Join Channel : @Nanthakps
</b>''')                                            # [Nanthakps](https://telegram.me/Nanthakps)

BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION",
'''<b>
🗂️ File : {file_name}

🏷 Size : {file_size}

📥 Join Channel : @Nanthakps
</b>''')                                            # [Nanthakps](https://telegram.me/Nanthakps)

IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE",
'''<b>
🏷 Title : {title}
🎭 Genres : {genres}
📆 Year : {year}
🌟 Rating : {rating} | IMDB</b>

<b>© Upload by : @Nanthakps
</b>''')                                            # [Nanthakps](https://telegram.me/Nanthakps)

LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

# EXTRA FEATURES
# URL Shortener
SHORTENER = environ.get('SHORTENER', '')                                # Recommended
SHORTENER_API = environ.get('SHORTENER_API', '')                        # Recommended

# Auto Delete For Group Message (Self Delete)
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

# Updates Button
UPDATES_BTN_NAME = "⚡️ ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ⚡️"                        # Recommended
UPDATES_BTN_URL = "https://telegram.me/Nanthakps"                       # Recommended

# Subscribe Button
SUBSCRIBE_BTN_NAME = "⚡️ ꜱᴜʙꜱᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟ ⚡️ "                         # Recommended
SUBSCRIBE_BTN_URL = "https://telegram.me/Nanthakps"                     # Recommended

# How To Download Button
DOWNLOAD_BTN_NAME = "⚡ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ⚡"                             # Recommended
DOWNLOAD_BTN_URL = "https://telegram.me/Nanthakps"                      # Recommended


## DEVELOPED BY ~ KPS 😎 ###
