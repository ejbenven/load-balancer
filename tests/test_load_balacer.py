import unittest
from .context import loadBalancer

class LoadBalancerTest(unittest.TestCase):

    def test_max_providers(self):
        """
        Check that we don't accept more providers than our capacity
        """
        N = 10
        lb = loadBalancer.LoadBalancer(N)
        for _ in range(N):
            provider = loadBalancer.Provider()
            lb.add_provider(provider)

        with self.assertRaises(BufferError):
            provider = loadBalancer.Provider()
            lb.add_provider(provider)


    def test_no_free_providers(self):
        lb = loadBalancer.LoadBalancer()
        self.assertEqual(lb.get(), "All providers are busy")


    def test_get_provider_random(self):
        """
        Check that we don't allocate the same provider twice
        Check that marking a provider busy doesn't allow us
        to add more providers to the load balancer when we are
        already at full capacity
        """
        N = 10
        lb = loadBalancer.LoadBalancer(N)
        for _ in range(N):
            provider = loadBalancer.Provider()
            lb.add_provider(provider)

        busy_providers = set()
        for i in range(N):
            provider_id, _ = lb._get_provider_random()
            self.assertTrue(provider_id not in busy_providers)
            busy_providers.add(provider_id)
            self.assertEqual(len(lb.free_providers), N - i - 1)

        with self.assertRaises(BufferError):
            provider = loadBalancer.Provider()
            lb.add_provider(provider)


    def test_round_robin_get(self):
        """
        Verify that the providers are invoked in the correct order
        and queued in the correct fashion with the round robin algorithm
        """
        N = 10
        lb = loadBalancer.LoadBalancer(N, False)
        for _ in range(N):
            provider = loadBalancer.Provider()
            lb.add_provider(provider)

        cpy = lb.free_providers.copy()
        ids = lb.free_providers.copy()
        for _ in range(N):
            self.assertEqual(ids.pop(), lb.get())

        self.assertTrue(cpy == lb.free_providers)


if __name__ == '__main__':
    unittest.main()
