import vk_api
import random
import time
#если вы не знаете что вообще за токен то посмотрите мой первый ролик на эту тему https://www.youtube.com/watch?v=n-b6HJ5R1c4&feature=youtu.be

#именной массив хранящий в себе имена групп и их токены
token = {
"group1":"fc417504ee6dda179607f59f3d175cb14c15287418881ba18909b56a6190db1d61804562d213e04b597fb" ,
"group2":"4f7ba2037a285926ad4e51a96071e426494dfbcbff5a253482572475e930987b0a2ce98f30b2bafda52d6",
"group3":"e6f4867cae9e8ad3048ed7cd88927b0caaa43b2bff240392ffc76b52cfa4ae6fcf4329d31fadc8f168a83"
}

#cозданый массив хранящий в себе ключь полученый с сервера
vks ={}
#функция получаящая ключи из токенов 
for i in token:
    vk = vk_api.VkApi(token=token[i])
    vk._auth_token()
    vks[i] = vk
print(vks)


while True:
    try:
        #
        for vki in vks:
            try:
                vk = vks[vki]
                messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
                if messages["count"] >= 1:
                    id = messages["items"][0]["last_message"]["from_id"]
                    body = messages["items"][0]["last_message"]["text"]
                    if body.lower() == "привет":
                        vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
                    elif body.lower() == "кто я?":
                        vk.method("messages.send", {"peer_id": id, "message": "ты хороший человек", "random_id": random.randint(1, 2147483647)})
                    

                    elif vki == "group1":
                        if body.lower() == "какая это группа":
                            vk.method("messages.send", {"peer_id": id, "message": "это группа "+ str(vki), "random_id": random.randint(1, 2147483647)})   

                        else:
                            vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})   
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})                        
            except Exception as e:
                print("ошибка в группе ",vki)
                pass

    except Exception as E:
        time.sleep(1)