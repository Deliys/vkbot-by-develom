import vk_api
import random
import time
#если вы не знаете что вообще за токен то посмотрите мой первый ролик на эту тему https://studio.youtube.com/video/DVKImJXVEDQ/edit
token = "ваш токен"


vk = vk_api.VkApi(token=token)

vk._auth_token()

dz = "дз нет"

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk.method("messages.send", {"peer_id": id, "message": "ты хороший человек", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "дз":
                vk.method("messages.send", {"peer_id": id, "message": str(dz), "random_id": random.randint(1, 2147483647)})
            else:
                a = list(body)
                b = 10
                data = ""
                while b>=0:
                    b = b - 1
                    data = str(data) + str(a[0])
                    a.pop(0)
                if data == "обновить дз":
                    b = len(a)
                    zap = ""
                    if b >=1:
                        for i in a:
                            zap = str(zap) + str(i)
                        dz = zap
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "дз нет", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)


