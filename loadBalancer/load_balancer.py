import threading
from random import choice
from collections import deque

class LoadBalancer:
    def __init__(self, max_providers=10, random=True):
        """
        max_providers: Maximum number of providers that can be registered
        random: If true, invokes providers randomly. Otherwise use round robin invocation
        """
        self.max_providers = max_providers
        self.providers = {}
        #For better bigO complexity we use a linked list for the round robin
        self.free_providers = [] if random else deque([])
        self.random = random
        self._lock = threading.Lock()

    def add_provider(self, provider):
        """
        Add provider to the list is it is not full
        """
        if len(self.providers) >= self.max_providers:
            raise BufferError("Provider list is full.")
        else:
            self.providers[provider.get()] = provider
            self.free_providers.append(provider.get())

    def _get_provider_random(self):
        """
        Return a random free provider
        """
        #We get a provider index at random
        free_provider_id = choice(range(len(self.free_providers)))
        provider_id = self.free_providers[free_provider_id]
        provider = self.providers[provider_id]
        self.free_providers[free_provider_id] = self.free_providers[-1]
        #We remove the index from the list
        self.free_providers.pop()

        return provider_id, provider

    def _get_provider_round_robin(self):
        provider_id = self.free_providers.pop()

        return provider_id, self.providers[provider_id]

    def get(self):
        """
        Send the GET request to a provider
        """
        provider = None
        provider_id = None
        with self._lock:
            if len(self.free_providers) == 0:
                return "All providers are busy"
            if(self.random):
                provider_id, provider = self._get_provider_random()
            else:
                provider_id, provider = self._get_provider_round_robin()

        val = provider.get()
        with self._lock:
            #The provider is now available again
            if self.random:
                self.free_providers.append(provider_id)
            else:
                self.free_providers.appendleft(provider_id)

        return val
