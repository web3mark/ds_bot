import time
import requests

tokens = []
with open("tokens.txt", "r") as f:
    for x in f.readlines():
        tokens.append(x.strip())

proxies = []
with open("proxies.txt", "r") as f:
    for x in f.readlines():
        proxies.append(x)


def send_message(tkn: str, proxy: str, channel_id: str, msg: str):
    headers = {"accept": "*/*",
               "accept-encoding": "gzip, deflate",
               "accept-language": "en-US",
               "authorization": tkn,
               "dnt": "1",
               "referer": "https://discord.com/channels/@me",
               "sec-ch-ua-mobile": "?0",
               "sec-ch-ua-platform": "\"Windows\"",
               "sec-fetch-dest": "empty",
               "sec-fetch-mode": "cors",
               "Content-Type": "application/json",
               "sec-fetch-site": "same-origin",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/108.0.0.0 Safari/537.36",
               "x-debug-options": "bugReporterEnabled",
               "x-discord-locale": "en-US"}
    content = {"content": msg}
    url = f"https://discord.com/api/v9/channels/{str(channel_id)}/messages"
    if proxy == "":
        response = requests.post(url=url,
                                 headers=headers,
                                 json=content)
        answer = response.json()
        print(answer["author"]["username"] + " sent message " + answer["content"] + " successfully")
    p = {'http': proxy,
         "https": proxy}
    response = requests.post(url=url,
                             headers=headers,
                             json=content,
                             proxies=p)
    answer = response.json()
    print(answer["author"]["username"] + " sent message " + answer["content"] + " successfully")


channelId = "1060736059215970345"  # сюда вписывать id канала, куда сообщения идут
while True:
    for i in range(len(tokens)):
        send_message(tokens[i], proxies[i % len(proxies)], channelId, "!work")
    time.sleep(60 * 60 + 5)
