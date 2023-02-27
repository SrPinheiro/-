import requests
import Function.requests.Information as DataCenter
import Function.taks.redirection as redirection
import Function.taks.map.updateMap as updateMe
import time

URL = DataCenter.getURL()
TOKEN = None
VERSION = 1.0
while True:
    try:
        if TOKEN == None:
            conn = requests.post(URL, json = DataCenter.getLogin())

            if conn.status_code == 201:
                TOKEN = conn.text
                DataCenter.writeToken(TOKEN)
            else:
                TOKEN = DataCenter.getLogin()["token"]
        else:
            param = {
                "version": VERSION,
                "token": DataCenter.getToken()
            }
            conn = requests.get(URL, json=param)
            if conn.status_code == 404:
                TOKEN = None
                continue
            elif conn.status_code == 204:
                pass
            elif conn.status_code == 424:
                updateMe.update()
            elif conn.status_code == 200 :
                response = conn.text.split(",")
                redirection.redirecionar(response)
            else:
                pass     
        time.sleep(0.5)

    except requests.exceptions.ConnectionError as err:
            print(err)
            print(err.__class__)
            print("CONNECTION ERRO")
            time.sleep(5)

    except Exception as err:
        print(err)
        print(err.__class__)
        print("Erro desconhecido!")
    