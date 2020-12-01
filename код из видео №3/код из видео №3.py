import vk_api
import random
import time
import json 

token = "ваш токен"


vk = vk_api.VkApi(token=token)
vk._auth_token()

file = open("data.txt" , "r")
data = json.load(file)

dz = data[0]
print(dz)
file.close()

def save():
    saves = []
    saves.append(dz)
    file = open("data.txt" , "w")
    json.dump(saves, file)
    file.close()
    

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }
keyboard = {
    "one_time": False,
    "buttons": [
    [get_button(label="привет", color="primary"),get_button(label="дз", color="negative")],
    [get_button(label="я люблю вк", color="positive"),get_button(label="develom", color="default")]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

#У кнопок может быть один из 4 цветов: 
#1. primary — синяя кнопка, обозначает основное действие. #5181B8 
#2. default — обычная белая кнопка. #FFFFFF 
#3. negative — опасное действие, или отрицательное действие (отклонить, удалить и тд). #E64646 
#4. positive — согласиться, подтвердить. #4BB34B
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
            elif body.lower() == "кнопки":
                vk.method("messages.send", {"peer_id": id, "keyboard": keyboard,"message": "вот и они", "random_id": random.randint(1, 2147483647)})

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
           
                save()
    except Exception as E:
        time.sleep(1)


