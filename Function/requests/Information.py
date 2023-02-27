import platform
from os import path

def getLogin():
    os = platform.system()
    machine  = platform.machine()
    user = platform.node()
    token = getToken()

    data = {
        "name": user,
        "os": os,
        "arquitetura": machine,
        "token": token
    }

    return data


def getToken():
    mainPath = path.join(path.expanduser(f"~/{platform.system()}"))
    try:
        with open(mainPath, "r") as file:
            token = file.read()

        return str(token)
    except:
        return None

def writeToken(token):
    teste = getLogin().get("os")
    mainPath = path.join(path.expanduser(f"~/{platform.system()}"))
    open(mainPath, "a").close()

    try:
        with open(mainPath, "w") as file:
            token = file.write(token)

        return token
    except FileNotFoundError:
        pass

def getURL():
    return "http://local.srpinheiro.com:8080"

        

if __name__ == "__main__":
    pass