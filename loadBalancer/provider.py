import threading

class Provider:
    id = 0
    lock = threading.Lock()

    def __init__(self, alive=True):
        """
        Create a provider with a unique ID
        For testing purposes, can define if provider is alive
        """
        with Provider.lock:
            self._id = Provider.id
            Provider.id += 1

        self.alive = alive

    def get(self):
        return f'{self._id}'

    def check(self):
        return self.alive
