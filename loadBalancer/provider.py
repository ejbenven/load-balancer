import threading
from time import sleep


class Provider:
    id = 0
    lock = threading.Lock()

    def __init__(self, alive=True, forever=True, delay=None):
        """
        Create a provider with a unique ID
        For testing purposes, can define if provider is alive
        If forerver is false, will toggle the alive status after the first check
        Wait delay seconds before returning the answer to the GET request
        """
        with Provider.lock:
            self._id = Provider.id
            Provider.id += 1

        self.alive = alive
        self.forever = forever
        self.delay = delay

    def get(self):
        if self.delay is not None:
            sleep(self.delay)
        return f"{self._id}"

    def check(self):
        alive = self.alive

        if not self.forever:
            self.forever = True
            self.alive = not self.alive
        return alive
