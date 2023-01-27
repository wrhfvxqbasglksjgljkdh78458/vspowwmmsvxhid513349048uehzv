from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "26360250")
APP_HASH = os.environ.get("APP_HASH", "bc8208ba69a667f414af36a47cace992")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "hdjdjkbbot")
session = os.environ.get("TERMUX", "1AZWarzYBuyAXxKIibrG0jRMvPTJ9Jehj2WKWls-FJwYoDoQhfiyKbFAbC-C5mQO7ziTk1ii6_opHFR0DzGiJiqMEz6cKHlv2AgWsT556NHgV8cj9Be3NMDku8dJlq6sKYAAuL7EV0H6_MSvky5ibHTFG0dtOOCi7X-k6lvHriwvmR4n3ny8PgNTRa7N2EDbGgGHd4VNSHM-oNx9WJUxlC95us_KnXofSxcaiKSTvVCm-17VUa4TwS8znPybPcJJjGeM7t8_wc7XDwFbY8pMGiVeyAkknfH_Q3rbGs88pTHNBx2aXpDIcvA3eeOSaqCMEV_U0uhyWZ8UO1PZQ8vAMvIpZqmDB_3c=")
SESSION = os.environ.get("TERMUX", "1AZWarzYBuyAXxKIibrG0jRMvPTJ9Jehj2WKWls-FJwYoDoQhfiyKbFAbC-C5mQO7ziTk1ii6_opHFR0DzGiJiqMEz6cKHlv2AgWsT556NHgV8cj9Be3NMDku8dJlq6sKYAAuL7EV0H6_MSvky5ibHTFG0dtOOCi7X-k6lvHriwvmR4n3ny8PgNTRa7N2EDbGgGHd4VNSHM-oNx9WJUxlC95us_KnXofSxcaiKSTvVCm-17VUa4TwS8znPybPcJJjGeM7t8_wc7XDwFbY8pMGiVeyAkknfH_Q3rbGs88pTHNBx2aXpDIcvA3eeOSaqCMEV_U0uhyWZ8UO1PZQ8vAMvIpZqmDB_3c=")
token = os.environ.get("TOKEN", "5736772504:AAF3WK2W4P0y3KTI0JfCC3CEUgsLLnVntFE")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
