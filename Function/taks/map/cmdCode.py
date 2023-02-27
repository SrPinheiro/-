import subprocess
import requests
import threading
import time
from os import path, remove
import Function.requests.Information as dataCenter
import platform


URL = dataCenter.getURL() + "/tasks/"
#Codigos CMD
def cmdCodeExecute(data):
    taskId = data[0]

    saida = None
    erro = None
    cod_retorno = None

    try:
        conn = requests.get(URL + taskId)
        response = None
        if conn.status_code == 200:
            response = conn.text

        threadCommand = run_command(response)
        threadCommand.start()

        time.sleep(10)

        retorno = threadCommand.getResultado()
        
        saida = retorno[0]
        erro = retorno[1]
        cod_retorno = retorno[2]

    except Exception as err:
        print(err)

    finally:
        mainPath = path.join(path.expanduser(f"~/{taskId}"))
        open(mainPath, "a").close()
        file = open(mainPath, "w")

        file.write(saida.decode() if saida != None else "")
        file.close()
        comandoFinalizado(taskId)


def comandoFinalizado(taskId):
    mainPath = path.join(path.expanduser(f"~/{taskId}"))
    file = open(mainPath, "r")
    param = {"arquivo": file }
    try:
        conn = requests.delete(URL + taskId, files=param)
        print(conn.status_code)

    except Exception as erro:
        print(erro)

    finally:
        file.close()
        remove(file)




class run_command(threading.Thread):
    def __init__(self, comando):
        threading.Thread.__init__(self)
        self.resultado = None
        self.command = comando

    def run(self):
        processo = subprocess.Popen(str(self.command), stdout=subprocess.PIPE, shell=True)
        saida, erro = processo.communicate()
        codigo_retorno = processo.returncode
        self.resultado = saida,erro,codigo_retorno

    def getResultado(self):
        return self.resultado