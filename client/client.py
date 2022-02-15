import requests
import pickle
import threading

"""     Error Codes
1: Connection Error
2: Data Recognition Error
"""

class KCCSClient:
    app: str = None
    host: str = None
    port: int = 0
    connected: bool = False
    uuid: float = -0.0
    auth: bool = False
    password: str
    username: str = None
    errorcallback = None

    def error(self, text, errorcode):
        print(f"[KCCS CLIENT ERROR][{errorcode}]: {text}")
        if self.errorcallback != None:
            self.errorcallback(text, errorcode)

    def __init__(self, host="localhost", port=57483, app="TEST", errorcallback=None, when_connected=None):
        self.port = port
        self.host = host
        self.app = app
        self.errorcallback = errorcallback
        self.when_connected = when_connected
        init_thread = threading.Thread(target=self._init_connection)
        init_thread.start()


    def _init_connection(self):
        try:
            requests.get(f"http://{self.host}:{self.port}/coninit")
            self.connected = True
            self.uuid = self.send(app="KCCS", method="request_uuid")
            self.when_connected()
        except Exception as e:
            self.error(f"KCCS could not connect to server: {e}", 1)


    def login(self, username, password):
        self.send(app="KCCS", method="login", args=[username, password])
        self.username = username
        self.password = password

    def logout(self):
        self.send(app="KCCS", method="logout")

    def send(self, method, args=None, app=None):
        if args == None:
            args = []
        if app == None:
            app = self.app
        if self.connected:
            try:
                ret = requests.post(f"http://{self.host}:{self.port}/send", data=pickle.dumps({"APP": app, "METHOD": method, "DATA": args, "UUID": self.uuid, "USER": self.username}))
                ret = pickle.loads(ret.content)
                if type(ret) == list:
                    if ret[0] == "!ERROR":
                        self.error(f"Data recognition error: {ret[1]}", 2)
                return ret
            except:
                self.error("KCCS not connected!", 1)
        else:
            self.error("KCCS not connected!", 1)
            return "ERR NOT CONNECTED"





"""
f = open("test.png", "rb")
data = f.read()
f.close()
url = 'http://127.0.0.1:57483/send'
x = requests.post(url, data=pickle.dumps({"APP": "TEST", "METHOD": "send", "DATA": data}))
"""
