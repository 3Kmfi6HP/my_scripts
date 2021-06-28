# 自动互助码到机器人
from telethon import TelegramClient, events
from numpy import random
from time import sleep
import requests, re, time, os

sleeptime = random.uniform(50, 100) #sleep 50~100 seconds
print("sleeping for:", sleeptime, "seconds")
sleep(sleeptime)
print("sleeping is over!")
farm = 'xxxx&aaaa&bbbb'
bean = ''
pet = ''
jxfactory = ''
health = ''
jxcfd = ''

api_id = '#######'
api_hash = '#######'
chat_id = '#######'
bot_token = '#######'
client = TelegramClient('telesession', api_id, api_hash)
        
def push():
    msg ={
        'chat_id': {chat_id},
        'text': f'助力码提交成功\n\n@JD_ShareCode_Bot',
        'disable_web_page_preview': 'true'
        }
    requests.post(url=f'https://api.telegram.org/bot{bot_token}/sendMessage', data=msg, timeout=15).json()

async def main():
    await client.send_message('JD_ShareCode_Bot', '/farm {farm}')
    await client.send_message('JD_ShareCode_Bot', '/bean {bean}')
    await client.send_message('JD_ShareCode_Bot', '/pet  {pet}')
    await client.send_message('JD_ShareCode_Bot', '/jxfactory {jxfactory}')
    await client.send_message('JD_ShareCode_Bot', '/health {health}')
    await client.send_message('JD_ShareCode_Bot', '/jxcfd {jxcfd}')
    await client.disconnect()
    push()

client.start()
client.loop.run_until_complete(main())
