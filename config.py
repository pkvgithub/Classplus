import os

API_ID = API_ID = 24709391

API_HASH = os.environ.get("API_HASH", "cb1ba6bba27a3c68d219e5e34419cb5e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6989792927:AAGKue_8JnrdDq_6OM0t3eG5694j9viHHG0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1923238241))

LOG = -1002030499286

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1923238241").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


