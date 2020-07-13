from loadBalancer import LoadBalancer, Provider
from time import sleep
import threading


def thread_function(lb):
    print(lb.get())


if __name__ == "__main__":
    N = 10
    lb = LoadBalancer(N, random=False)
    for _ in range(N - 3):
        provider = Provider(delay=1)
        lb.add_provider(provider)

    lb.add_provider(Provider(alive=False, delay=1))
    lb.add_provider(Provider(alive=False, forever=False, delay=1))
    lb.add_provider(Provider(alive=True, forever=False, delay=1))

    for i in range(50):
        x = threading.Thread(target=thread_function, args=(lb,))
        x.start()
        if i % 10 == 0:
            sleep(1)
