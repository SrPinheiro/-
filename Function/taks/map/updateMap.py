import os
from urllib import request
# import Function.requests.Information as DataCenter

ROTA = "/download-last"
def update():
    URL = "http://local.srpinheiro.com:8080/download/last"
    file = "files/update.zip"
    request.urlretrieve(URL , file)

    try:
        os.system("unzip files/update.zip -d files/")
        os.system("rm files/update.zip")
        os.system("python3 files/main.py")
    except:
        print("ERRO")

update()