class Cooler(object):
    """ Various convenience methods to make things cooler. """

    pedro = 1

    def add_man(self, sentence):
        """ End a sentence with ", man!" to make it sound cooler, and
        return the result. """
        return sentence + ", man!"

    def add_42(self, n):
        """ Add 42 to an integer argument to make it cooler, and return the
        result. """
        return n + 42

    def boat(self, sentence):
        """ Replace a sentence with "I'm on a boat!", and return that,
        because it's cooler. """
        return "I'm on a boat!"

    def add_pedro(self):
        self.pedro = self.pedro + 1
        return "pedro is now {0}".format(self.pedro)


import zerorpc

s = zerorpc.Server(Cooler())
s.bind("tcp://0.0.0.0:4242")
s.run()
