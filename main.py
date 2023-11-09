import random
import requests
import time

tokens = []
with open("tokens.txt", "r") as f:
    for x in f.readlines():
        tokens.append(x)

while True:
    for token in tokens:
        headers = {"accept": "*/*",
               "accept-encoding": "gzip, deflate",
               "accept-language": "en-US",
               "authorization": token,
               "dnt": "1",
               "referer": "https://discord.com/channels/@me",
               "sec-ch-ua-mobile": "?0",
               "sec-ch-ua-platform": "\"Windows\"",
               "sec-fetch-dest": "empty",
               "sec-fetch-mode": "cors",
               'Content-Type': 'application/json',
               "sec-fetch-site": "same-origin",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
               "x-debug-options": "bugReporterEnabled", "x-discord-locale": "en-US"}
        content = {"content": "Hello, World!"} # вместо hello world свое сообщение
        channel_id = "877979516557987911" # id канала, куда отправляются сообщения
        try:
            send_message = requests.post(url=f"https://discord.com/api/v9/channels/{channel_id}/messages", json=content,
                                         headers=headers)
            print(send_message.json())
        except:
            print("Отправить сообщение не удалось")
    print("Все сообщения отправлены, скрипт ждёт час")
    time.sleep(random.randint(3400, 3800))