# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "4906250"))
API_HASH = getenv("API_HASH", "0ce8e2006b20d73d5582a894acf26b33")
BOT_TOKEN = getenv("BOT_TOKEN", "7185157515:AAHT-zYxWtQl-nGZM0yYi7IumyEoE7a4WTQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5145411673").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://saver:admin123@cluster0.idpixx4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1001904634429")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001663631966"))
