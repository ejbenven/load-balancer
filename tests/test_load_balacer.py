import unittest
from .context import loadBalancer

class LoadBalancerTest(unittest.TestCase):

    def test_max_providers(self):
        N = 10
        lb = loadBalancer.LoadBalancer(N)
        for _ in range(N):
            provider = loadBalancer.Provider()
            lb.add_provider(provider)

        with self.assertRaises(BufferError):
            provider = loadBalancer.Provider()
            lb.add_provider(provider)


if __name__ == '__main__':
    unittest.main()
