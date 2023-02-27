import Function.taks.map.cmdCode as cmdCode
import Function.taks.map.screenCheck as SC

def redirecionar(taskInfoHash):
    if taskInfoHash[1] == "1":
        cmdCode.cmdCodeExecute(taskInfoHash)
    if taskInfoHash[1] == "2":
        SC.screenLock()


