from loadBalancer import LoadBalancer, Provider
from time import sleep

if __name__ == "__main__":
    N = 10
    lb = LoadBalancer(N)
    for _ in range(N):
        provider = Provider()
        lb.add_provider(provider)


    for i in range(50):
        print(lb.get())
        if i % 10 == 0:
            sleep(1)
