import zerorpc


class ZeroClient:
    # Here will be the instance stored.
    __instance = None

    c = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ZeroClient.__instance == None:
            ZeroClient()
        return ZeroClient.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ZeroClient.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ZeroClient.__instance = self
            self.c = zerorpc.Client()
            self.c.connect("tcp://data:4242")  # "data" is the containers name
