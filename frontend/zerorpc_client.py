import zerorpc


class ZerorpcClient:
    __shared_state = {}
    c = None

    def __init__(self):
        self.__dict__ = self.__shared_state

        self.c = zerorpc.Client()
        self.c.connect("tcp://0.0.0.0:4242")  # "data" is the containers name

    def get_state(self):
        return self.c
