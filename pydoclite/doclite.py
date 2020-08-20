from ctypes import *
import json,platform,os,sys

class NoLibException(Exception):
    pass

sharedlibpath = os.path.join(
    os.getcwd(),
    "{}/docliteshared.so".format(
        platform.system().casefold()
    )
)

paths=[sharedlibpath]+list(
    map(
        lambda x:os.path.join(x,"pydoclite/docliteshared.so"),
        sys.path
    )
)

for path in paths:
    try:
        if os.stat(path):
            break
    except FileNotFoundError:
        sharedlibpath = path
else:
    raise NoLibException("shared Lib not found")


deleted=b'deleted'

class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]

lib = cdll.LoadLibrary(sharedlibpath)
lib.ConnectDB.argtypes = [GoString]
lib.Close.argtypes = []


lib.Insert.argtypes = [GoString]
lib.Insert.restype = GoString

lib.FindOne.argtypes = [c_longlong, GoString]
lib.FindOne.restype = GoString

lib.Find.argtypes = [GoString,GoString]
lib.Find.restype = GoString

lib.Delete.argtypes = [GoString,GoString]


class Collection:
    def __init__(self,name:str):
        self.name = name

    def GetCollection(self,name:str):
        if "|" in name:
            raise ValueError("name cannot contain alphanumeric")
        return Collection("{}|{}".format(self.name,name))
    
    def Insert(self,document:dict):
        document = json.dumps(document).encode()
        name = self.name.encode()
        return lib.Insert(
            GoString(document, len(document)),
            GoString(name, len(name))
        )

    def FindOne(self,id):
        name = self.name.encode()
        res = lib.FindOne(
            id,
            GoString(name, len(name)),
        ).p
        if not res or res==deleted:
            return {}
        return json.loads(res)

    def Find(self,filter):
        filter = json.dumps(filter).encode()
        name = self.name.encode()
        res=lib.Find(
            GoString(name, len(name)),
            GoString(filter, len(filter)),
        ).p
        if not res:
            return []
        return json.loads(res)

    def DeleteOne(self,id):
        name = self.name.encode()
        lib.DeleteOne(
            id,
            GoString(name, len(name)),
        )

    def Delete(self,filter):
        filter = json.dumps(filter).encode()
        name = self.name.encode()
        lib.Delete(
            GoString(name, len(name)),
            GoString(filter, len(filter)),
        )

class Doclite:
    @staticmethod
    def Connect(name:str):
        filename  = GoString(name, len(name))
        lib.ConnectDB(filename)
        return Doclite()
    
    def Close(self):
        lib.Close()

    def Base(self):
        return Collection("")