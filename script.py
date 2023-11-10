import time
import requests

# Getting information from files
tokens = []
proxies = []
with open("tokens.txt", "r") as f:
    for x in f.readlines():
        tokens.append(x.strip())
with open("proxies.txt", "r") as f:
    for x in f.readlines():
        proxies.append(x)


class User:
    def __init__(self, token):
        self._token = token
        self._headers = {"accept": "*/*",
                   "accept-encoding": "gzip, deflate",
                   "accept-language": "en-US",
                   "authorization": self._token,
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

    def send_message(self, channel_id: str, msg: str, proxy=""):
        headers = self._headers
        content = {"content": msg}
        url = f"https://discord.com/api/v9/channels/{str(channel_id)}/messages"
        if proxy == "":
            response = requests.post(url=url,
                                     headers=headers,
                                     json=content)
            answer = response.json()
            print(answer["author"]["username"] + " sent message " + answer["content"] + " successfully")
        else:
            p = {'http': proxy,
                 "https": proxy}
            response = requests.post(url=url,
                                     headers=headers,
                                     json=content,
                                     proxies=p)
            answer = response.json()
            print(answer["author"]["username"] + " sent message " + answer["content"] + " successfully")


channelId = "1060736059215970345"  # channel id
delay = 3605  # delay in seconds


# Here you can write your own code
def main():
    while True:
        for i in range(len(tokens)):
            User(tokens[i]).send_message(channelId, "!work", proxy=proxies[i % len(proxies) - 1])
        time.sleep(delay)


if __name__ == "__main__":
    main()
